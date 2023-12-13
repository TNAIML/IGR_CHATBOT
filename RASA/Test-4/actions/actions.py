
import time
import subprocess
import ast

from typing import Any, Text, Dict, List

from rasa_sdk import Action , Tracker , FormValidationAction 
from rasa_sdk.events import EventType 
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted, AllSlotsReset , UserUtteranceReverted

from rasa_sdk.events import SlotSet 

from pathlib import Path


lang_layer = {'1':'Tamil','2':'English'}

Main_layer_en = {'1':'Document_Registration','2':'Encumbrance_Certificate','3':'View_Encumbrance_Certificate' ,'4':'certified_copy','5':'Marriage_Registration', '6':'Firm_Registration','7':'society_Registration','8':'Payment_Refund_Service','9':'Token_Service','10':'Online_Index_Correction','11':'Online_Registration','12':'further_clarrification_other_queries','13':'Go_Back'}
Main_layer_tn = {'1':'Document_Registration','2':'Encumbrance_Certificate','3':'View_Encumbrance_Certificate' ,'4':'certified_copy','5':'Marriage_Registration', '6':'Firm_Registration','7':'society_Registration','8':'Payment_Refund_Service','9':'Token_Service','10':'Online_Index_Correction','11':'Online_Registration','12':'further_clarrification_other_queries','13':'Go_Back'}


en_Document_Registration  =  {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'Go_back'}
en_Encumbrance_Certificate =  {'1':'1','2':'2','3':'Go_back'}
en_View_Encumbrance_Certificate =  {'1':'1','2':'Go_back'}
en_certified_copy =  {'1':'1','2':'2','3':'Go_back'}
en_Marriage_Registration =   {'1':'1','2':'2','3':'3','4':'Go_back'}
en_Firm_Registration =   {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'Go_back'}
en_society_Registration =    {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'Go_back'}
en_Payment_Refund_Service = {'1':'1','2':'2','3':'Go_back'}
en_Token_Service = {'1':'1','2':'Go_back'}
en_Online_Index_Correction = {'1':'1','2':'Go_back'}
en_Online_Registration = {'1':'1','2':'Go_back'}
en_further_clarrification_other_queries = {'1':'1','2':'2','3':'Go_back'}



tn_Document_Registration  =  {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'Go_back'}
tn_Encumbrance_Certificate =  {'1':'1','2':'2','3':'Go_back'}
tn_View_Encumbrance_Certificate =  {'1':'1','2':'Go_back'}
tn_certified_copy =  {'1':'1','2':'2','3':'Go_back'}
tn_Marriage_Registration =   {'1':'1','2':'2','3':'3','4':'Go_back'}
tn_Firm_Registration =   {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'Go_back'}
tn_society_Registration =    {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'Go_back'}
tn_Payment_Refund_Service = {'1':'1','2':'2','3':'Go_back',}
tn_Token_Service = {'1':'1','2':'Go_back'}
tn_Online_Index_Correction = {'1':'1','2':'Go_back'}
tn_Online_Registration = {'1':'1','2':'Go_back'}
tn_further_clarrification_other_queries = {'1':'1','2':'2','3':'Go_back'}



Document_Registration_l1_1 = {'1':'1'}
Document_Registration_l1_2 = {'1':'1'}
Document_Registration_l1_3 = {'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'Go_back'}
Document_Registration_l1_4  =  {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'11','12':'12','13':'13','14':'14','15':'15','16':'16','17':'Go_back'}
Document_Registration_l1_5 = {'1':'https://drive.google.com/file/d/1dn_8LcttdT-mKzrBOkwJcqeRD9ymJOJ_/view?usp=share_link','2':'https://youtu.be/DGfzc2Gr7qQ','3':'Go_back'}
Document_Registration_l1_6 = {'1':'https://drive.google.com/file/d/1uSRwlYrBgMY1HBes09D_EQ3As063wIb-/view?usp=share_link','3':'Go_back'}
Document_Registration_l1_7 = {'1':'https://drive.google.com/file/d/1MNd678V8XnfFouvbCxQBrEeShVoOOCAT/view?usp=share_link','2':'Go_back'}        



Document_Registration_l2_1 =  {'1':'https://drive.google.com/file/d/14FRKniE-STxtUhOPGtfvgG8TNQc3N_w2/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_2 =  {'1':'https://drive.google.com/file/d/1SKxaZaqNNdI-bLnu5tCPjREytwwrm13X/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_3 =  {'1':'https://drive.google.com/file/d/1XxaM8qsq_zPI0HPRxomjPPu21cXV5dSD/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_4 =  {'1':'https://drive.google.com/file/d/1Z_PIietGAklTQx1j84BAh9Cse3gvkb3F/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_5 =  {'1':'https://drive.google.com/file/d/1Ryk0hEUYT0tlgTY8Odvk_Bk8jEkX436q/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_6 =  {'1':'https://drive.google.com/file/d/1xC5lR1wORmSROBNc0GlXSMf6MxO40vHc/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_7 =  {'1':'https://drive.google.com/file/d/1qQ8iiPqqakWrgzcbbt6tg_SJAAus6p9B/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_8 =  {'1':'https://drive.google.com/file/d/1n1mdhKUY0hIHct2FLOwyWxQmdKOv2tMR/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_9 =  {'1':'https://drive.google.com/file/d/1zE0tjZ1g91eFBCVggEOX1uu6by_QcWNX/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_10 = {'1':'https://drive.google.com/file/d/1Ryk0hEUYT0tlgTY8Odvk_Bk8jEkX436q/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_11 = {'1':'https://drive.google.com/file/d/1h_d40pvlzGZeK93l9KNOgomV3RnhgSee/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_12 = {'1':'https://drive.google.com/file/d/13lLE0WZHck9lfU2KO43a9hSSZNDiJwpT/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_13 = {'1':'https://drive.google.com/file/d/1Yj0zzLzc64m4Zj0e0vIKkr6Ta-dfBtIg/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_14 = {'1':'https://drive.google.com/file/d/1euqUCdKDBQGZb5dTI8md2NzjmCMko3sb/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_15 = {'1':'https://drive.google.com/file/d/1fr2L0h72A80bU5_N-z7saQD4bL7RKAEt/view?usp=share_link','2':'Go_back'}
Document_Registration_l2_16 = {'1':'https://drive.google.com/file/d/1EILNtOx9EjSUwxgCH_-ybDEqNCabb1Tf/view?usp=share_link','2':'Go_back'}



Encumbrance_Certificate_l1_1 = {'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'Go_back'}
Encumbrance_Certificate_l1_2 = {'1':'https://drive.google.com/file/d/1L6FYTFWm7Da6wCv_42MLoYspn8BsW8jL/view?usp=share_link','2':'https://youtu.be/lQIiDDFt3r8','3':'Go_back'}


View_Encumbrance_Certificate = {'1':'https://youtu.be/KzewqPueKSo','2':'Go_back'}


certified_copy_l1_1 = {'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'Go_back'}
certified_copy_l1_2 = {'1':'https://drive.google.com/file/d/1eCfz24LihS1jmyIDP7gIK4NugpojB9wK/view?usp=share_link','2':'https://youtu.be/Q-hLENwwdAw2v','3':'Go_back'}



Marriage_Registration_l1_1 = {'1':'1','2':'2','3':'3','4':'4','5':'Go_back'}
Marriage_Registration_l1_2 ={'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'https://drive.google.com/file/d/1SP5CtsOy3o5X109wltwiqnlnTJKez_CT/view?usp=share_link','4':'https://drive.google.com/file/d/17Bu4mQ5PyLbZxvJr6K36-iU_5VY1vo_E/view?usp=share_link','5':'https://drive.google.com/file/d/1bJDyWZhb6BWWgJziyIxtFNlpiRhJRG5N/view?usp=share_link','6':'https://drive.google.com/file/d/1G98mAY3NVW4ntkLyGPBAsgFEDT6lhww6/view?usp=share_link','7':'https://youtu.be/d-u2sgcek4w','8':'Go_back'} 
Marriage_Registration_l1_3 ={'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'https://drive.google.com/file/d/16dpXNRNRbGUrNhmi8x0yR1M6XEAXY-BX/view?usp=share_link','4':'https://drive.google.com/file/d/1l5CXP4JZw71iDHHX6xJ_8TgUzgDpxnex/view?usp=share_link','5':'https://drive.google.com/file/d/1l5CXP4JZw71iDHHX6xJ_8TgUzgDpxnex/view?usp=share_link','6':'https://drive.google.com/file/d/1aLeUdKg0plsAGRun1BZdxkCYoDBedL4P/view?usp=share_link','7':'https://youtu.be/d-u2sgcek4w','8':'Go_back'}  
Marriage_Registration_l2_1 ={'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'https://drive.google.com/file/d/1hypW05nRc5-iyzWDOCpsH4p3Jw2EuYNe/view?usp=share_link','4':'https://youtu.be/G32_uE-k7xY','5':'Go_back'} 
Marriage_Registration_l2_2 ={'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'https://drive.google.com/file/d/1Abq5N-nVRHfAFFWSjDOrzhUD3DK3dXgx/view?usp=share_link','4':'https://youtu.be/G32_uE-k7xY','5':'Go_back'} 
Marriage_Registration_l2_3 ={'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'https://drive.google.com/file/d/1hn5EtB2iRKbyzC3yKG3DzJ_xYeDVXBo9/view?usp=share_link','4':'https://youtu.be/4mXjrEUpoUs','5':'https://drive.google.com/file/d/15ljUhSMHnmZy183RtCFxs5Dp3o1v-isC/view?usp=share_link','6':'https://youtu.be/4mXjrEUpoUs','7':'Go_back'} 
Marriage_Registration_l2_4 ={'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'https://drive.google.com/file/d/1fPr5dPKqoGhIJ-E0Tb2_WjdaJLasuaJ_/view?usp=share_link','4':'Go_back'}                                                                                                     


Firm_Registration_l1_1 ={'1':'https://drive.google.com/file/d/1EM5DOtEHY1pBTJ22yj0GtlOa_VPceZsi/view?usp=share_link','2':'https://youtu.be/XKDLTNsr4hw','3':'Go_back'} 
Firm_Registration_l1_2 ={'1':'https://drive.google.com/file/d/1PK_tUYLw7_h-Lhv_xBgpSpUCLhYcr0OE/view?usp=share_link','2':'Go_back'} 
Firm_Registration_l1_3 ={'1':'https://drive.google.com/file/d/1gFMzhyxyqg9v0ZSCBGw-QsrxK_lHTNrJ/view?usp=share_link','2':'Go_back'} 
Firm_Registration_l1_4 ={'1':'https://drive.google.com/file/d/12nE3LnUrPcvOhJ4p6wF_0JQrDpyw7sKD/view?usp=share_link','2':'Go_back'} 
Firm_Registration_l1_5 ={'1':'https://drive.google.com/file/d/1BPBDYIaNlct1_08kKCIjtFlSD0auXd6W/view?usp=share_link','2':'Go_back'} 
Firm_Registration_l1_6 ={'1':'https://drive.google.com/file/d/1f0CCngIqiVNz9FWT4CV-Ug-VGe9tgA3A/view?usp=share_link','2':'Go_back'} 
Firm_Registration_l1_7 ={'1':'https://drive.google.com/file/d/1Uy8qBbazHC7JYXDal6O5MYAsB86h-xwF/view?usp=share_link','2':'Go_back'} 



society_Registration_l1_1 = {'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'Go_back'} 
society_Registration_l1_2 = {'1':'https://drive.google.com/file/d/16kZ81MBU7T3P86BngIiQv2yizVLbNc3W/view?usp=share_link','2':'Go_back'} 
society_Registration_l1_3 = {'1':'https://drive.google.com/file/d/1OJn7H6XzjonpP61nzD3hPB-TLWf6Ebpy/view?usp=share_link','2':'Go_back'} 
society_Registration_l1_4 = {'1':'https://drive.google.com/file/d/1UU9G6JILp7kr-tTyWZW6rEjVslGryHlC/view?usp=share_link','2':'Go_back'} 
society_Registration_l1_5 = {'1':'https://drive.google.com/file/d/1nomjBojnldHVWpbVUTf0fCeBz35CiLNe/view?usp=share_link','2':'Go_back'} 

Payment_Refund_Service_l1_1 = {'1':'https://youtu.be/BVeUVw0M-sU','2':'Go_back'}
Payment_Refund_Service_l1_2 = {'1':'https://youtu.be/wV3TjPot5p0','2':'Go_back'}


Token_Service= {'1':'https://youtu.be/i1mOdYeqE1U','2':'Go_back'}

Online_Index_Correction = {'1':'https://drive.google.com/file/d/1MNd678V8XnfFouvbCxQBrEeShVoOOCAT/view?usp=drive_link','2':'Go_back'}

Online_Registration = {'1':'https://drive.google.com/file/d/1OVeAYNqDQfssNVjm6aHWHsRQfB-uSlvc/view?usp=drive_link','2':'Go_back'}

further_clarrification_other_queries_l1_1 = {'1':'1'}
further_clarrification_other_queries_l1_2 = {'1':'1'}


tn_Document_Registration_l1_1 = {'1':'1'}
tn_Document_Registration_l1_2 = {'1':'1'}
tn_Document_Registration_l1_3 = {'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'Go_back'}        
tn_Document_Registration_l1_4  =  {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','11':'11','12':'12','13':'13','14':'14','15':'15','16':'16','17':'Go_back'}
tn_Document_Registration_l1_5 = {'1':'https://drive.google.com/file/d/1dn_8LcttdT-mKzrBOkwJcqeRD9ymJOJ_/view?usp=share_link','2':'https://youtu.be/DGfzc2Gr7qQ','3':'Go_back'}
tn_Document_Registration_l1_6 = {'1':'https://drive.google.com/file/d/1uSRwlYrBgMY1HBes09D_EQ3As063wIb-/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l1_7 = {'1':'https://drive.google.com/file/d/1MNd678V8XnfFouvbCxQBrEeShVoOOCAT/view?usp=share_link','2':'Go_back'}        



tn_Document_Registration_l2_1 =  {'1':'https://drive.google.com/file/d/1CUCkXefRA-aqj3mRM-1mN2z_gauHL6xT/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_2 =  {'1':'https://drive.google.com/file/d/1lf_-Qra2Hnkw4BUdBuwmehuSSHRtn5jQ/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_3 =  {'1':'https://drive.google.com/file/d/1fPSetCeYeGP36bCzEgbkK_83p0L1fF_2/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_4 =  {'1':'https://drive.google.com/file/d/1TWxol6d4JBrQ2ST32TxQUMIK_FssCgjn/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_5 =  {'1':'https://drive.google.com/file/d/1HLPikHQ2sZPWEzn9k8ALL772evuuC60V/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_6 =  {'1':'https://drive.google.com/file/d/1xC5lR1wORmSROBNc0GlXSMf6MxO40vHc/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_7 =  {'1':'https://drive.google.com/file/d/1DYa6Hp8MEDUVxT8-zIEpLVrIcm-UPw3N/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_8 =  {'1':'https://drive.google.com/file/d/1g3n7Djv4SgM1FSTJTDPB7otiCE1YRfPg/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_9 =  {'1':'https://drive.google.com/file/d/1LYHjO8331whiO9y7FAksWtK9n2vV8h0u/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_10 = {'1':'https://drive.google.com/file/d/1-MfWKwScx_2ynjhuZJ_NzwIlsOJaE5s3/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_11 = {'1':'https://drive.google.com/file/d/1E7bebKtcKWGt3duYHVP4LznePIf5VG85/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_12 = {'1':'https://drive.google.com/file/d/1rEXFOhPPeis4FhjhSS9MtHmI6Eh8PslB/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_13 = {'1':'https://drive.google.com/file/d/1Sv9FabHAm6Ld8JbjiOAWOAWKtcUmRDQN/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_14 = {'1':'https://drive.google.com/file/d/1Flp_C5MaLaCMzXKOMuLN3C3tWcD0eA3E/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_15 = {'1':'https://drive.google.com/file/d/1CAxeDCj1fw1j-Rf4mZOcBsAGUm6vNOS8/view?usp=share_link','2':'Go_back'}
tn_Document_Registration_l2_16 = {'1':'https://drive.google.com/file/d/18OUYZrn4jiT-pz4SvwR2VcIFrSpNdzLa/view?usp=share_link','2':'Go_back'}



# en_Encumbrance_Certificate_l1 = {'1':'1','2':'2','3':'Go_back'}
tn_Encumbrance_Certificate_l1_1 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','3':'Go_back'}
tn_Encumbrance_Certificate_l1_2 = {'1':'https://drive.google.com/file/d/1L6FYTFWm7Da6wCv_42MLoYspn8BsW8jL/view?usp=share_link','2':'https://youtu.be/lQIiDDFt3r8','3':'Go_back'}

tn_View_Encumbrance_Certificate_1 = {'1':'https://youtu.be/KzewqPueKSo','2':'Go_back'}

tn_certified_copy_l1_1 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','3':'Go_back'}
tn_certified_copy_l1_2 = {'1':'https://drive.google.com/file/d/1eCfz24LihS1jmyIDP7gIK4NugpojB9wK/view?usp=share_link','2':'https://youtu.be/Q-hLENwwdAw','3':'Go_back'}

tn_Marriage_Registration_l1_1 = {'1':'1','2':'2','3':'3','4':'4','5':'Go_back'}
tn_Marriage_Registration_l1_2 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'2v','3':'https://drive.google.com/file/d/1SP5CtsOy3o5X109wltwiqnlnTJKez_CT/view?usp=share_link','4':'https://drive.google.com/file/d/17Bu4mQ5PyLbZxvJr6K36-iU_5VY1vo_E/view?usp=share_link','5':'https://drive.google.com/file/d/1bJDyWZhb6BWWgJziyIxtFNlpiRhJRG5N/view?usp=share_link','6':'https://drive.google.com/file/d/1G98mAY3NVW4ntkLyGPBAsgFEDT6lhww6/view?usp=share_link','7':'7','8':'Go_back'}
tn_Marriage_Registration_l1_3 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'2v','3':'https://drive.google.com/file/d/16dpXNRNRbGUrNhmi8x0yR1M6XEAXY-BX/view?usp=share_link','4':'https://drive.google.com/file/d/1l5CXP4JZw71iDHHX6xJ_8TgUzgDpxnex/view?usp=share_link','5':'https://drive.google.com/file/d/1l5CXP4JZw71iDHHX6xJ_8TgUzgDpxnex/view?usp=share_link','6':'https://drive.google.com/file/d/1aLeUdKg0plsAGRun1BZdxkCYoDBedL4P/view?usp=share_link','7':'7','8':'Go_back'} 
tn_Marriage_Registration_l2_1 = {'1':'https://drive.google.com/file/d/1foXtq3OZJcVfJD456Bjp49aom6eulICh/view?usp=share_link','2':'2v','3':'https://drive.google.com/file/d/1hypW05nRc5-iyzWDOCpsH4p3Jw2EuYNe/view?usp=share_link','4':'1v','5':'Go_back'}
tn_Marriage_Registration_l2_2 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'2v','3':'https://drive.google.com/file/d/1Abq5N-nVRHfAFFWSjDOrzhUD3DK3dXgx/view?usp=share_link','4':'2v','5':'Go_back'}
tn_Marriage_Registration_l2_3 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'3v','3':'https://drive.google.com/file/d/1hn5EtB2iRKbyzC3yKG3DzJ_xYeDVXBo9/view?usp=share_link','4':'https://youtu.be/4mXjrEUpoUs','5':'https://drive.google.com/file/d/15ljUhSMHnmZy183RtCFxs5Dp3o1v-isC/view?usp=share_link','6':'','7':'Go_back'}
tn_Marriage_Registration_l2_4 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'2v','3':'https://drive.google.com/file/d/1fPr5dPKqoGhIJ-E0Tb2_WjdaJLasuaJ_/view?usp=share_link','4':'4v','5':'Go_back'}                                                                                                     

tn_Firm_Registration_l1_1 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'https://youtu.be/XKDLTNsr4hw','3':'Go_back'}
tn_Firm_Registration_l1_2 = {'1':'https://drive.google.com/file/d/1PK_tUYLw7_h-Lhv_xBgpSpUCLhYcr0OE/view?usp=share_link','2':'Go_back'}
tn_Firm_Registration_l1_3 = {'1':'https://drive.google.com/file/d/1gFMzhyxyqg9v0ZSCBGw-QsrxK_lHTNrJ/view?usp=share_link','2':'Go_back'}
tn_Firm_Registration_l1_4 = {'1':'https://drive.google.com/file/d/12nE3LnUrPcvOhJ4p6wF_0JQrDpyw7sKD/view?usp=share_link','2':'Go_back'}
tn_Firm_Registration_l1_5 = {'1':'https://drive.google.com/file/d/1BPBDYIaNlct1_08kKCIjtFlSD0auXd6W/view?usp=share_link','2':'Go_back'}
tn_Firm_Registration_l1_6 = {'1':'https://drive.google.com/file/d/1f0CCngIqiVNz9FWT4CV-Ug-VGe9tgA3A/view?usp=share_link','2':'Go_back'}
tn_Firm_Registration_l1_7 = {'1':'https://drive.google.com/file/d/1Uy8qBbazHC7JYXDal6O5MYAsB86h-xwF/view?usp=share_link','2':'Go_back'}

tn_society_Registration_l1_1 = {'1':'https://drive.google.com/file/d/19Pq6-21DhHesOLLyeydyueyB5Z2-Mgrl/view?usp=share_link','2':'https://youtu.be/Rlq7W7TlOVk','3':'Go_back'}
tn_society_Registration_l1_2 = {'1':'https://drive.google.com/file/d/16kZ81MBU7T3P86BngIiQv2yizVLbNc3W/view?usp=share_link','2':'Go_back'}
tn_society_Registration_l1_3 = {'1':'https://drive.google.com/file/d/1OJn7H6XzjonpP61nzD3hPB-TLWf6Ebpy/view?usp=share_link','2':'Go_back'}
tn_society_Registration_l1_4 = {'1':'https://drive.google.com/file/d/1UU9G6JILp7kr-tTyWZW6rEjVslGryHlC/view?usp=share_link','2':'Go_back'}
tn_society_Registration_l1_5 = {'1':'https://drive.google.com/file/d/1nomjBojnldHVWpbVUTf0fCeBz35CiLNe/view?usp=share_link','2':'Go_back'}

tn_Payment_Refund_Service_l1_1 = {'1':'https://youtu.be/BVeUVw0M-sU','2':'Go_back'}
tn_Payment_Refund_Service_l1_2 = {'1':'https://youtu.be/wV3TjPot5p0','2':'Go_back'}


tn_Token_Service_1= {'1':'https://youtu.be/i1mOdYeqE1U','2':'Go_back'}

tn_Online_Index_Correction_1 = {'1':'https://drive.google.com/file/d/1MNd678V8XnfFouvbCxQBrEeShVoOOCAT/view?usp=drive_link','2':'Go_back'}

tn_Online_Registration_1 = {'1':'https://drive.google.com/file/d/1OVeAYNqDQfssNVjm6aHWHsRQfB-uSlvc/view?usp=drive_link','2':'Go_back'}


tn_further_clarrification_other_queries_l1_1 = {'1':'1'}
tn_further_clarrification_other_queries_l1_2 = {'1':'1'}



v = ''
w = ''
x = ''
y = ''
z = ''



class ValidateBotForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_bot_form_1"


    def validate_choices_1(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `choices_1` value."""


        global v
        global y
        global w 
        global x 
        global Z
        
        slot_1 = tracker.get_slot('choices_1')
        lang_selection = lang_layer.get( slot_1)
        if lang_selection == 'Tamil':
            v = 'Tamil'
            y = None
            w = None
            x = None
            Z = None
            dispatcher.utter_message(response = "utter_main_layer_tn")
        elif lang_selection == 'English':
            v = 'English'
            y = None
            w = None
            x = None
            Z = None
            dispatcher.utter_message(response = "utter_main_layer_en")



        if lang_selection not in list(lang_layer.values()):

            dispatcher.utter_message(response = "utter_ask_lang_valid_responce")
            return {"choices_1": None}
            
        
        
        return {"choices_1": slot_value}



    def validate_choices_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `Choices_2` value."""

        global v
        global w
        global y

        slot_2 = tracker.get_slot('choices_2')
        main_selection_en = Main_layer_en.get( slot_2)
        main_selection_tn = Main_layer_tn.get( slot_2)
        
        if (v == 'English'):
            
           
            if main_selection_en == 'Document_Registration':
                w = 'Document_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Document_Registration")
            elif main_selection_en == 'Encumbrance_Certificate':
                w = 'Encumbrance_Certificate'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Encumbrance_Certificate")
            elif main_selection_en == 'View_Encumbrance_Certificate':
                w = 'View_Encumbrance_Certificate'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_View_Encumbrance_Certificate")
            elif main_selection_en == 'certified_copy':
                w = 'certified_copy'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_certified_copy")
            elif main_selection_en == 'Marriage_Registration':
                w = 'Marriage_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Marriage_Registration")
            elif main_selection_en == 'Firm_Registration':
                w = 'Firm_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Firm_Registration")
            elif main_selection_en == 'society_Registration':
                w = 'society_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_society_Registration")
            elif main_selection_en == 'Payment_Refund_Service':
                w = 'Payment_Refund_Service'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Payment_and_Refund_of_payment")               
            elif main_selection_en == 'Token_Service':
                w = 'Token_Service'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Token_Service")
            elif main_selection_en == 'Online_Index_Correction':
                w = 'Online_Index_Correction'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Online_Index_Correction")
            elif main_selection_en == 'Online_Registration':
                w = 'Online_Registration'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_Online_Registration")
            elif main_selection_en == 'further_clarrification_other_queries':
                w = 'further_clarrification_other_queries'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_en_If_any_further_clarrification_other_queries")
            elif main_selection_en == 'Go_Back':
                dispatcher.utter_message(response = "utter_lang_selection")
                return {"choices_1": None ,"choices_2": None , "choices_1": None}
            # tn_Online_Registration_1
            elif main_selection_en not in list(Main_layer_en.values()):
                dispatcher.utter_message(response = "utter_ask_valid_responce")
                return {"choices_2": None}
    

        elif (v == 'Tamil'):
           
            if main_selection_tn == 'Document_Registration':
                w = 'Document_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Document_Registration")
            elif main_selection_tn == 'Encumbrance_Certificate':
                w = 'Encumbrance_Certificate'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Encumbrance_Certificate")
            elif main_selection_tn == 'View_Encumbrance_Certificate':
                w = 'View_Encumbrance_Certificate'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_View_Encumbrance_Certificate")
            elif main_selection_tn == 'certified_copy':
                w = 'certified_copy'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_certified_copy")
            elif main_selection_tn == 'Marriage_Registration':
                w = 'Marriage_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Marriage_Registration")
            elif main_selection_tn == 'Firm_Registration':
                w = 'Firm_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Firm_Registration")
            elif main_selection_tn == 'society_Registration':
                w = 'society_Registration'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_society_Registration")
            #issue fixed
            elif main_selection_tn == 'Payment_Refund_Service':
                w = 'Payment_Refund_Service'
                #Working 
                # dispatcher.utter_message(response = "utter_ask_2nd_layer_tamil_Payment_and_Refund_of_payment")
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Payment_and_refund_of_payment")
                print(main_selection_tn)
            elif main_selection_tn == 'Token_Service':
                w = 'Token_Service'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Token_Service")
            elif main_selection_tn == 'Online_Index_Correction':
                w = 'Online_Index_Correction'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Online_Index_Correction")
            elif main_selection_tn == 'Online_Registration':
                w = 'Online_Registration'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_Online_Registration")
            elif main_selection_tn == 'further_clarrification_other_queries':
                w = 'further_clarrification_other_queries'
                y = 'third_layer'
                dispatcher.utter_message(response = "utter_ask_2nd_layer_tn_If_any_further_clarrification_other_queries")
            elif main_selection_tn == 'Go_Back':
                dispatcher.utter_message(response = "utter_lang_selection")
                return {"choices_2": None , "choices_1": None}
            elif main_selection_tn not in list(Main_layer_tn.values()):
                dispatcher.utter_message(response = "utter_ask_valid_responce")
                return {"choices_2": None}


        return {"choices_2": slot_value}
    

    def validate_choices_3(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `Choices_3` value."""

        slot_3 = tracker.get_slot('choices_3')
        third_selection_dc= en_Document_Registration.get(slot_3)
        third_selection_ec= en_Encumbrance_Certificate.get(slot_3)
        third_selection_vec= View_Encumbrance_Certificate.get(slot_3)
        third_selection_cc= en_certified_copy.get(slot_3)
        third_selection_mr= en_Marriage_Registration.get(slot_3)
        third_selection_fr= en_Firm_Registration.get(slot_3)
        third_selection_sr= en_society_Registration.get(slot_3)
        third_selection_pr= en_Payment_Refund_Service.get(slot_3)
        third_selection_et = Token_Service.get(slot_3)
        third_selection_oic= Online_Index_Correction.get(slot_3)
        third_selection_or= Online_Registration.get(slot_3)
        third_selection_afc= en_further_clarrification_other_queries.get(slot_3)

        tn_third_selection_dc= tn_Document_Registration.get(slot_3)
        tn_third_selection_ec= tn_Encumbrance_Certificate.get(slot_3)
        tn_third_selection_vec= tn_View_Encumbrance_Certificate_1.get(slot_3)
        tn_third_selection_cc= tn_certified_copy.get(slot_3)
        tn_third_selection_mr= tn_Marriage_Registration.get(slot_3)
        tn_third_selection_fr= tn_Firm_Registration.get(slot_3)
        tn_third_selection_sr= tn_society_Registration.get(slot_3)
        tn_third_selection_pr= tn_Payment_Refund_Service.get(slot_3)
        tn_third_selection_et = tn_Token_Service_1.get(slot_3)
        tn_third_selection_oic= tn_Online_Index_Correction_1.get(slot_3)
        tn_third_selection_or= tn_Online_Registration_1.get(slot_3)
        tn_third_selection_afc=tn_further_clarrification_other_queries.get(slot_3)


        global w
        global x
        global y
        global z


        if (v == 'English'):

            if w == 'Document_Registration':
            
                if third_selection_dc == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_1'
                    y = 'third_layer'
                    time.sleep(3)
                elif third_selection_dc == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_2'
                    y = 'third_layer'
                    time.sleep(3)
                elif third_selection_dc == '3':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_3'
                    time.sleep(3)
                elif third_selection_dc == '4':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_4' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_4'
                    y = 'last_layer'
                    time.sleep(3)
                elif third_selection_dc == '5':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_5' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_5'
                    time.sleep(3)
                elif third_selection_dc == '6':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_6' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_6'
                    time.sleep(3)
                elif third_selection_dc == '7':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Document_Registration_l1_7' )
                    x = 'utter_ask_2nd_layer_en_Document_Registration_l1_7'
                    time.sleep(3)
                    # dispatcher.utter_message(response ='utter_lang_selection')
                
                elif  third_selection_dc == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_en')
                    return {"choices_2": None, "choices_3": None}
                    # return {"choices_1": None,"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Encumbrance_Certificate':       
                if third_selection_ec == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Encumbrance_Certificate_l1_1' )
                    x = 'utter_ask_2nd_layer_en_Encumbrance_Certificate_l1_1' 
                    time.sleep(3)
                elif third_selection_ec == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Encumbrance_Certificate_l1_2' )
                    x = 'utter_ask_2nd_layer_en_Encumbrance_Certificate_l1_2'
                    time.sleep(3)
# 
                elif  third_selection_ec == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'View_Encumbrance_Certificate':       
                if slot_3 in list(View_Encumbrance_Certificate.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_en' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = third_selection_vec)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    



            elif w == 'certified_copy':
                if third_selection_cc == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_certified_copy_l1_1')
                    x = 'utter_ask_2nd_layer_en_certified_copy_l1_1'
                    time.sleep(3)
                elif third_selection_cc == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_certified_copy_l1_2' )
                    x = 'utter_ask_2nd_layer_en_certified_copy_l1_2'
                    time.sleep(3)
                elif  third_selection_cc == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Marriage_Registration':           
                if third_selection_mr == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_en_Marriage_Registration_l1_1'
                    y = 'last_layer'
                    time.sleep(3)
                elif third_selection_mr == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_en_Marriage_Registration_l1_2'
                    time.sleep(3)
                elif third_selection_mr == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_en_Marriage_Registration_l1_3'
                    time.sleep(3)
                elif  third_selection_mr == 'Go_back':
                    dispatcher.utter_message(response = 'utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Firm_Registration':            
                if third_selection_fr == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_1'
                    time.sleep(3)
                elif third_selection_fr == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_2'
                    time.sleep(3)
                elif third_selection_fr == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_3'
                    time.sleep(3)
                elif third_selection_fr == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_4' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_4'
                    time.sleep(3)
                elif third_selection_fr == '5':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_5' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_5'
                    time.sleep(3)
                elif third_selection_fr == '6':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_6' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_6'
                    time.sleep(3)
                elif third_selection_fr == '7':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Firm_Registration_l1_7' )
                    x = 'utter_ask_2nd_layer_en_Firm_Registration_l1_7'
                    time.sleep(3)
                elif third_selection_fr == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}



            elif w == 'society_Registration':            
                if third_selection_sr == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_society_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_en_society_Registration_l1_1'
                    time.sleep(3)
                elif third_selection_sr == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_society_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_en_society_Registration_l1_2'
                    time.sleep(3)
                elif third_selection_sr == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_society_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_en_society_Registration_l1_3'
                    time.sleep(3)
                elif third_selection_sr == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_society_Registration_l1_4' )
                    x = 'utter_ask_2nd_layer_en_society_Registration_l1_4'
                    time.sleep(3)
                elif third_selection_sr == '5':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_society_Registration_l1_5' )
                    x = 'utter_ask_2nd_layer_en_society_Registration_l1_5'
                    time.sleep(3)
                elif  third_selection_sr == 'Go_back':
                    dispatcher.utter_message(response = 'utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Payment_Refund_Service':
                if third_selection_pr == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Payment_and_Refund_of_payment_l1_1')
                    x = 'utter_ask_2nd_layer_en_Payment_and_Refund_of_payment_l1_1'
                    time.sleep(3)
                elif third_selection_pr == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_en_Payment_and_Refund_of_payment_l1_2' )
                    x = 'utter_ask_2nd_layer_en_Payment_and_Refund_of_payment_l1_2'
                    time.sleep(3)
                elif  third_selection_pr == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}



            elif w == 'Token_Service':
                if slot_3 in list(Token_Service.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_en' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = third_selection_et)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    


            elif w == 'Online_Index_Correction':
                if slot_3 in list(Online_Index_Correction.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_en' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = third_selection_oic)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    


            elif w == 'Online_Registration':
                if slot_3 in list(Online_Registration.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_en' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = third_selection_or)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    



            elif w == 'further_clarrification_other_queries':           
                if third_selection_afc == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_If_any_further_clarrification_other_queries_l1_1' )
                    time.sleep(3)
                elif third_selection_afc == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_If_any_further_clarrification_other_queries_l1_2' )
                    time.sleep(3)
                elif  third_selection_afc == 'Go_back':
                    dispatcher.utter_message(response = 'utter_main_layer_en' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


        if (v == 'Tamil'):

            if w == 'Document_Registration':
        
                if tn_third_selection_dc == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_1'
                    y = 'third_layer'
                    time.sleep(3)
                elif tn_third_selection_dc == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_2'
                    y = 'third_layer'
                    time.sleep(3)
                elif tn_third_selection_dc == '3':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_3'
                    time.sleep(3)
                elif tn_third_selection_dc == '4':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_4' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_4'
                    y = 'last_layer'
                    time.sleep(3)
                elif tn_third_selection_dc == '5':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_5' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_5'
                    time.sleep(3)
                elif tn_third_selection_dc == '6':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_6' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_6'
                    time.sleep(3)
                elif tn_third_selection_dc == '7':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Document_Registration_l1_7' )
                    x = 'utter_ask_2nd_layer_tn_Document_Registration_l1_7'
                    time.sleep(3)
                elif  tn_third_selection_dc == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Encumbrance_Certificate':       
                if tn_third_selection_ec == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Encumbrance_Certificate_l1_1' )
                    x = 'utter_ask_2nd_layer_tn_Encumbrance_Certificate_l1_1' 
                    time.sleep(3)
                elif tn_third_selection_ec == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Encumbrance_Certificate_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_Encumbrance_Certificate_l1_2'
                    time.sleep(3)
                elif  tn_third_selection_ec == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}

            elif w == 'View_Encumbrance_Certificate':       
                if slot_3 in list(tn_View_Encumbrance_Certificate.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_tn' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = tn_third_selection_vec)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    


            elif w == 'certified_copy':
                if tn_third_selection_cc == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_certified_copy_l1_1')
                    x = 'utter_ask_2nd_layer_tn_certified_copy_l1_1'
                    time.sleep(3)
                elif tn_third_selection_cc == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_certified_copy_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_certified_copy_l1_2'
                    time.sleep(3)
                elif  tn_third_selection_cc == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Marriage_Registration':           
                if tn_third_selection_mr == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_1'
                    y = 'last_layer'
                    time.sleep(3)
                elif tn_third_selection_mr == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_2'
                    time.sleep(3)
                elif tn_third_selection_mr == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_3'
                    time.sleep(3)
                elif  tn_third_selection_mr == 'Go_back':
                    dispatcher.utter_message(response = 'utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Firm_Registration':            
                if tn_third_selection_fr == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_1'
                    time.sleep(3)
                elif tn_third_selection_fr == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_2'
                    time.sleep(3)
                elif tn_third_selection_fr == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_3'
                    time.sleep(3)
                elif tn_third_selection_fr == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_4' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_4'
                    time.sleep(3)
                elif tn_third_selection_fr == '5':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_5' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_5'
                    time.sleep(3)
                elif tn_third_selection_fr == '6':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_6' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_6'
                    time.sleep(3)
                elif tn_third_selection_fr == '7':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_7' )
                    x = 'utter_ask_2nd_layer_tn_Firm_Registration_l1_7'
                    time.sleep(3)
                elif third_selection_fr == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}

            elif w == 'society_Registration':            
                if tn_third_selection_sr == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_society_Registration_l1_1' )
                    x = 'utter_ask_2nd_layer_tn_society_Registration_l1_1'
                    time.sleep(3)
                elif tn_third_selection_sr == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_society_Registration_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_society_Registration_l1_2'
                    time.sleep(3)
                elif tn_third_selection_sr == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_society_Registration_l1_3' )
                    x = 'utter_ask_2nd_layer_tn_society_Registration_l1_3'
                    time.sleep(3)
                elif tn_third_selection_sr == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_society_Registration_l1_4' )
                    x = 'utter_ask_2nd_layer_tn_society_Registration_l1_4'
                    time.sleep(3)
                elif tn_third_selection_sr == '5':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_society_Registration_l1_5' )
                    x = 'utter_ask_2nd_layer_tn_society_Registration_l1_5'
                    time.sleep(3)
                elif  tn_third_selection_sr == 'Go_back':
                    dispatcher.utter_message(response = 'utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}


            elif w == 'Payment_Refund_Service':
                if tn_third_selection_pr == '1':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Payment_and_refund_of_payment_l1_1')
                    x = 'utter_ask_2nd_layer_tn_Payment_and_refund_of_payment_l1_1'
                    time.sleep(3)
                elif tn_third_selection_pr == '2':
                    dispatcher.utter_message(response ='utter_ask_2nd_layer_tn_Payment_and_refund_of_payment_l1_2' )
                    x = 'utter_ask_2nd_layer_tn_Payment_and_refund_of_payment_l1_2'
                    time.sleep(3)
                elif  tn_third_selection_pr == 'Go_back':
                    dispatcher.utter_message(response ='utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}



            elif w == 'Token_Service':
                if slot_3 in list(tn_Token_Service.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_tn' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = tn_third_selection_et)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    


            elif w == 'Online_Index_Correction':
                if slot_3 in list(Online_Index_Correction.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_tn' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = tn_third_selection_oic)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    



            elif w == 'Online_Registration':
                if slot_3 in list(tn_Online_Registration_1.keys()):
                    if slot_3 == '2':
                        dispatcher.utter_message(response = 'utter_main_layer_tn' )
                        return {"choices_2": None,"choices_3": None}
                    else:
                        dispatcher.utter_message(text = tn_third_selection_or)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}    


            elif w == 'further_clarrification_other_queries':           
                if tn_third_selection_afc == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_If_any_further_clarrification_other_queries_l1_1' )
                    time.sleep(3)
                elif tn_third_selection_afc == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_If_any_further_clarrification_other_queries_l1_2' )
                    time.sleep(3)
                elif  tn_third_selection_afc == 'Go_back':
                    dispatcher.utter_message(response = 'utter_main_layer_tn' )
                    return {"choices_2": None, "choices_3": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_3": None}



        if y != 'third_layer':
            return {"requested_slot": "choices_4" }
        else:
            return {"requested_slot": None  }





    def validate_choices_4(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `Choices_3` value."""


        slot_4 = tracker.get_slot('choices_4')
        

        global x
        global y
        global z

        fourth_selection_dr3  = Document_Registration_l1_3 .get(slot_4)
        fourth_selection_dr4  = Document_Registration_l1_4 .get(slot_4)
        fourth_selection_dr5  = Document_Registration_l1_5 .get(slot_4)
        fourth_selection_dr6  = Document_Registration_l1_6 .get(slot_4)
        fourth_selection_dr7  = Document_Registration_l1_7 .get(slot_4)
       
        fourth_selection_ec1 = Encumbrance_Certificate_l1_1.get(slot_4)
        fourth_selection_ec2 = Encumbrance_Certificate_l1_2.get(slot_4)
       
        fourth_selection_cc1 = certified_copy_l1_1.get(slot_4)
        fourth_selection_cc2 = certified_copy_l1_2.get(slot_4)
       
        fourth_selection_mr1 = Marriage_Registration_l1_1.get(slot_4)
        fourth_selection_mr2 = Marriage_Registration_l1_2.get(slot_4)
        fourth_selection_mr3 = Marriage_Registration_l1_3.get(slot_4)


        fourth_selection_fr1 = Firm_Registration_l1_1.get(slot_4)
        fourth_selection_fr2 = Firm_Registration_l1_2.get(slot_4)
        fourth_selection_fr3 = Firm_Registration_l1_3.get(slot_4)
        fourth_selection_fr4 = Firm_Registration_l1_4.get(slot_4)
        fourth_selection_fr5 = Firm_Registration_l1_5.get(slot_4)
        fourth_selection_fr6 = Firm_Registration_l1_6.get(slot_4)
        fourth_selection_fr7 = Firm_Registration_l1_7.get(slot_4)
        
        fourth_selection_sr1 = society_Registration_l1_1.get(slot_4)
        fourth_selection_sr2 = society_Registration_l1_2.get(slot_4)
        fourth_selection_sr3 = society_Registration_l1_3.get(slot_4)
        fourth_selection_sr4 = society_Registration_l1_4.get(slot_4)
        fourth_selection_sr5 = society_Registration_l1_5.get(slot_4)

        fourth_selection_pt1 =  Payment_Refund_Service_l1_1.get(slot_4)
        fourth_selection_pt2 =  Payment_Refund_Service_l1_2.get(slot_4)

       
                

        tn_fourth_selection_dr3  = tn_Document_Registration_l1_3 .get(slot_4)
        tn_fourth_selection_dr4  = tn_Document_Registration_l1_4 .get(slot_4)
        tn_fourth_selection_dr5  = tn_Document_Registration_l1_5 .get(slot_4)
        tn_fourth_selection_dr6  = tn_Document_Registration_l1_6 .get(slot_4)
        tn_fourth_selection_dr7  = tn_Document_Registration_l1_7 .get(slot_4)
       
        tn_fourth_selection_ec1 = tn_Encumbrance_Certificate_l1_1.get(slot_4)
        tn_fourth_selection_ec2 = tn_Encumbrance_Certificate_l1_2.get(slot_4)
       
        tn_fourth_selection_cc1 = tn_certified_copy_l1_1.get(slot_4)
        tn_fourth_selection_cc2 = tn_certified_copy_l1_2.get(slot_4)
       
        tn_fourth_selection_mr1 = tn_Marriage_Registration_l1_1.get(slot_4)
        tn_fourth_selection_mr2 = tn_Marriage_Registration_l1_2.get(slot_4)
        tn_fourth_selection_mr3 = tn_Marriage_Registration_l1_3.get(slot_4)


        tn_fourth_selection_fr1 = tn_Firm_Registration_l1_1.get(slot_4)
        tn_fourth_selection_fr2 = tn_Firm_Registration_l1_2.get(slot_4)
        tn_fourth_selection_fr3 = tn_Firm_Registration_l1_3.get(slot_4)
        tn_fourth_selection_fr4 = tn_Firm_Registration_l1_4.get(slot_4)
        tn_fourth_selection_fr5 = tn_Firm_Registration_l1_5.get(slot_4)
        tn_fourth_selection_fr6 = tn_Firm_Registration_l1_6.get(slot_4)
        tn_fourth_selection_fr7 = tn_Firm_Registration_l1_7.get(slot_4)
        
        tn_fourth_selection_sr1 = tn_society_Registration_l1_1.get(slot_4)
        tn_fourth_selection_sr2 = tn_society_Registration_l1_2.get(slot_4)
        tn_fourth_selection_sr3 = tn_society_Registration_l1_3.get(slot_4)
        tn_fourth_selection_sr4 = tn_society_Registration_l1_4.get(slot_4)
        tn_fourth_selection_sr5 = tn_society_Registration_l1_5.get(slot_4)
        

        tn_fourth_selection_pt1 =  tn_Payment_Refund_Service_l1_1.get(slot_4)
        tn_fourth_selection_pt2 =  tn_Payment_Refund_Service_l1_2.get(slot_4)
        



        if (v == 'English'):

            if x == 'utter_ask_2nd_layer_en_Document_Registration_l1_3' :

                if slot_4 in list(Document_Registration_l1_3.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_dr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    
            if x == 'utter_ask_2nd_layer_en_Document_Registration_l1_4' :
                if fourth_selection_dr4 == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_1' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_1'
                    time.sleep(3)
                elif fourth_selection_dr4 == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_2' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_2'
                    time.sleep(3)
                elif fourth_selection_dr4 == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_3' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_3'
                    time.sleep(3)
                elif fourth_selection_dr4 == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_4' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_4'
                    time.sleep(3)
                elif fourth_selection_dr4 == '5':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_5' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_5'
                    time.sleep(3)
                elif fourth_selection_dr4 == '6':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_6' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_6'
                    time.sleep(3)
                elif fourth_selection_dr4 == '7':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_7' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_7'
                    time.sleep(3)
                elif fourth_selection_dr4 == '8':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_8' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_8'
                    time.sleep(3)
                elif fourth_selection_dr4 == '9':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_9' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_9'
                    time.sleep(3)
                elif fourth_selection_dr4 == '10':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_10' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_10'
                    time.sleep(3)
                elif fourth_selection_dr4 == '11':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_11' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_11'
                    time.sleep(3)
                elif fourth_selection_dr4 == '12':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_12' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_12'
                    time.sleep(3)
                elif fourth_selection_dr4 == '13':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_13' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_13'
                    time.sleep(3)
                elif fourth_selection_dr4 == '14':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_14' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_14'
                    time.sleep(3)
                elif fourth_selection_dr4 == '15':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_15' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_15'
                    time.sleep(3)
                elif fourth_selection_dr4 == '16':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Document_Registration_l2_16' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Document_Registration_l2_16'
                    time.sleep(3)
                elif  fourth_selection_dr4 == 'Go_back':
                    dispatcher.utter_message(response = 'utter_lang_selection' )
                    return {"choices_1": None,"choices_2": None, "choices_3": None,"choices_4": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            if x == 'utter_ask_2nd_layer_en_Document_Registration_l1_5' :

                if slot_4 in list(Document_Registration_l1_5.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_dr5)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    
 
            if x == 'utter_ask_2nd_layer_en_Document_Registration_l1_6' :

                if slot_4 in list(Document_Registration_l1_6.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_dr6)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    

            if x == 'utter_ask_2nd_layer_en_Document_Registration_l1_7' :
                if slot_4 in list(Document_Registration_l1_7.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_dr7)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    

  
    
            elif x == 'utter_ask_2nd_layer_en_Encumbrance_Certificate_l1_1' :

                if slot_4 in list(Encumbrance_Certificate_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_ec1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    
            elif x == 'utter_ask_2nd_layer_en_Encumbrance_Certificate_l1_2':
                if slot_4 in list(Encumbrance_Certificate_l1_2.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_ec2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            elif x == 'utter_ask_2nd_layer_en_certified_copy_l1_1':
                if slot_4 in list(certified_copy_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_cc1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_certified_copy_l1_2':
                if slot_4 in list(certified_copy_l1_2.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_cc2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            elif x == 'utter_ask_2nd_layer_en_Marriage_Registration_l1_1':   
                if fourth_selection_mr1 == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l2_1' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_en_Marriage_Registration_l2_1'
                    time.sleep(3)
                elif fourth_selection_mr1 == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l2_2' )
                    y = 'last_layer'
                    z= 'utter_ask_2nd_layer_en_Marriage_Registration_l2_2'
                    time.sleep(3)
                elif fourth_selection_mr1 == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l2_3' )
                    y = 'last_layer'
                    z= 'utter_ask_2nd_layer_en_Marriage_Registration_l2_3'
                    time.sleep(3)
                elif fourth_selection_mr1 == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_en_Marriage_Registration_l2_4' )
                    y = 'last_layer'
                    z= 'utter_ask_2nd_layer_en_Marriage_Registration_l2_4'
                    time.sleep(3)
                elif  fourth_selection_mr1 == 'Go_back':
                    dispatcher.utter_message(response = 'utter_lang_selection' )
                    return {"choices_1": None,"choices_2": None, "choices_3": None,"choices_4": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Marriage_Registration_l1_2':
                if slot_4 in list(Marriage_Registration_l1_2.keys()):
                    if slot_4 == '8':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_mr2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Marriage_Registration_l1_3':
                if slot_4 in list(Marriage_Registration_l1_3.keys()):
                    if slot_4 == '8':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_mr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_1':
                if slot_4 in list(Firm_Registration_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_2':
                if slot_4 in list(Firm_Registration_l1_2.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_3':
                if slot_4 in list(Firm_Registration_l1_3.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection')
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_4':
                if slot_4 in list(Firm_Registration_l1_4.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr4)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_5':
                if slot_4 in list(Firm_Registration_l1_5.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr5)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_6':
                if slot_4 in list(Firm_Registration_l1_6.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr6)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Firm_Registration_l1_7':
                if slot_4 in list(Firm_Registration_l1_7.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  fourth_selection_fr7)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}




            elif x == 'utter_ask_2nd_layer_en_society_Registration_l1_1':
                if slot_4 in list(society_Registration_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =fourth_selection_sr1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_society_Registration_l1_2':
                if slot_4 in list(society_Registration_l1_2.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_sr2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_society_Registration_l1_3':
                if slot_4 in list(society_Registration_l1_3.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_sr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_society_Registration_l1_4':
                if slot_4 in list(society_Registration_l1_4.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_sr4)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_society_Registration_l1_5':
                if slot_4 in list(society_Registration_l1_5.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_sr5)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            elif x == 'utter_ask_2nd_layer_en_Payment_and_Refund_of_payment_l1_1':
                if slot_4 in list(Payment_Refund_Service_l1_1.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_pt1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_en_Payment_and_Refund_of_payment_l1_2':
                if slot_4 in list(Payment_Refund_Service_l1_2.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = fourth_selection_pt2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}



        if (v == 'Tamil'):

            if x == 'utter_ask_2nd_layer_tn_Document_Registration_l1_3' :

                if slot_4 in list(tn_Document_Registration_l1_3.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_dr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    
            if x == 'utter_ask_2nd_layer_tn_Document_Registration_l1_4' :
                if tn_fourth_selection_dr4 == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_1' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_1'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_2' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_2'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_3' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_3'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_4' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_4'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '5':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_5' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_5'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '6':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_6' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_6'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '7':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_7' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_7'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '8':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_8' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_8'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '9':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_9' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_9'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '10':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_10' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_10'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '11':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_11' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_11'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '12':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_12' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_12'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '13':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_13' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_13'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '14':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_14' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_14'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '15':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_15' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_15'
                    time.sleep(3)
                elif tn_fourth_selection_dr4 == '16':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Document_Registration_l2_16' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Document_Registration_l2_16'
                    time.sleep(3)
                elif  tn_fourth_selection_dr4 == 'Go_back':
                    dispatcher.utter_message(response = 'utter_lang_selection' )
                    return {"choices_1": None,"choices_2": None, "choices_3": None,"choices_4": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}

            if x == 'utter_ask_2nd_layer_tn_Document_Registration_l1_5' :

                if slot_4 in list(tn_Document_Registration_l1_5.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_dr5)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    

            if x == 'utter_ask_2nd_layer_tn_Document_Registration_l1_6' :
                if slot_4 in list(tn_Document_Registration_l1_6.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_dr6)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    

            if x == 'utter_ask_2nd_layer_tn_Document_Registration_l1_7' :

                if slot_4 in list(tn_Document_Registration_l1_7.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_dr7)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}    



            elif x == 'utter_ask_2nd_layer_tn_Encumbrance_Certificate_l1_1' :

                if slot_4 in list(tn_Encumbrance_Certificate_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_ec1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


    
            elif x == 'utter_ask_2nd_layer_tn_Encumbrance_Certificate_l1_2':
                if slot_4 in list(tn_Encumbrance_Certificate_l1_2.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_ec2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}



            elif x == 'utter_ask_2nd_layer_tn_certified_copy_l1_1':
                if slot_4 in list(tn_certified_copy_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_cc1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_certified_copy_l1_2':
                if slot_4 in list(tn_certified_copy_l1_2.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_cc2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            elif x == 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_1':   
                if tn_fourth_selection_mr1 == '1':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_1' )
                    y = 'last_layer'
                    z = 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_1'
                    time.sleep(3)
                elif tn_fourth_selection_mr1 == '2':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_2' )
                    y = 'last_layer'
                    z= 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_2'
                    time.sleep(3)
                elif tn_fourth_selection_mr1 == '3':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_3' )
                    y = 'last_layer'
                    z= 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_3'
                    time.sleep(3)
                elif tn_fourth_selection_mr1 == '4':
                    dispatcher.utter_message(response = 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_4' )
                    y = 'last_layer'
                    z= 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_4'
                    time.sleep(3)
                elif  tn_fourth_selection_mr1 == 'Go_back':
                    dispatcher.utter_message(response = 'utter_lang_selection' )
                    return {"choices_1": None,"choices_2": None, "choices_3": None,"choices_4": None}
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_2':
                if slot_4 in list(tn_Marriage_Registration_l1_2.keys()):
                    if slot_4 == '8':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =tn_fourth_selection_mr2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Marriage_Registration_l1_3':
                if slot_4 in list(tn_Marriage_Registration_l1_3.keys()):
                    if slot_4 == '8':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_mr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            elif x == 'utter_ask_2nd_layer_tn_Firm_Registration_l1_1':
                if slot_4 in list(tn_Firm_Registration_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Firm_Registration_l1_2':
                if slot_4 in list(tn_Firm_Registration_l1_2.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Firm_Registration_l1_3':
                if slot_4 in list(tn_Firm_Registration_l1_3.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection')
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == ' utter_ask_2nd_layer_tn_Firm_Registration_l1_4':
                if slot_4 in list(tn_Firm_Registration_l1_4.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr4)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Firm_Registration_l1_5':
                if slot_4 in list(tn_Firm_Registration_l1_5.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr5)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Firm_Registration_l1_6':
                if slot_4 in list(tn_Firm_Registration_l1_6.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr6)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Firm_Registration_l1_7':
                if slot_4 in list(tn_Firm_Registration_l1_7.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =  tn_fourth_selection_fr7)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}


            if x == 'utter_ask_2nd_layer_tn_society_Registration_l1_1':
                if slot_4 in list(tn_society_Registration_l1_1.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text =tn_fourth_selection_sr1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_society_Registration_l1_2':
                if slot_4 in list(tn_society_Registration_l1_2.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_sr2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_society_Registration_l1_3':
                if slot_4 in list(tn_society_Registration_l1_3.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_sr3)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_society_Registration_l1_4':
                if slot_4 in list(tn_society_Registration_l1_4.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_sr4)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_society_Registration_l1_5':
                if slot_4 in list(tn_society_Registration_l1_5.keys()):
                    if slot_4 == '3':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_sr5)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
    

            elif x == 'utter_ask_2nd_layer_tn_Payment_and_refund_of_payment_l1_1':
                if slot_4 in list(tn_Payment_Refund_Service_l1_1.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_pt1)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}
            elif x == 'utter_ask_2nd_layer_tn_Payment_and_refund_of_payment_l1_2':
                if slot_4 in list(tn_Payment_Refund_Service_l1_2.keys()):
                    if slot_4 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None}
                    else:
                        dispatcher.utter_message(text = tn_fourth_selection_pt2)
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_4": None}




       # The above code is a Python if-else statement. It checks if the value of the variable `y` is
       # equal to the string `'last_layer'`. If it is, it returns a dictionary with the key
       # `"requested_slot"` set to the string `"choices_5"`. If `y` is not equal to `'last_layer'`, it
       # returns a dictionary with the key `"requested_slot"` set to `None`.
        if y == 'last_layer':
            return {"requested_slot": "choices_5" }
        else:
            return {"requested_slot": None  }



    def validate_choices_5(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `choices_5` value."""

        global y

        slot_5 = tracker.get_slot('choices_5')

        fifth_selection_l2dr1 =Document_Registration_l2_1.get(slot_5)
        fifth_selection_l2dr2 =Document_Registration_l2_2.get(slot_5)
        fifth_selection_l2dr3 =Document_Registration_l2_3.get(slot_5)
        fifth_selection_l2dr4 =Document_Registration_l2_4.get(slot_5)
        fifth_selection_l2dr5 =Document_Registration_l2_5.get(slot_5)
        fifth_selection_l2dr6 =Document_Registration_l2_6.get(slot_5)
        fifth_selection_l2dr7 =Document_Registration_l2_7.get(slot_5)
        fifth_selection_l2dr8 =Document_Registration_l2_8.get(slot_5)
        fifth_selection_l2dr9 =Document_Registration_l2_9.get(slot_5)
        fifth_selection_l2dr10 =Document_Registration_l2_10.get(slot_5)
        fifth_selection_l2dr11 =Document_Registration_l2_11.get(slot_5)
        fifth_selection_l2dr12 =Document_Registration_l2_12.get(slot_5)
        fifth_selection_l2dr13 =Document_Registration_l2_13.get(slot_5)
        fifth_selection_l2dr14 =Document_Registration_l2_14.get(slot_5)
        fifth_selection_l2dr15 =Document_Registration_l2_15.get(slot_5)
        fifth_selection_l2dr16 =Document_Registration_l2_16.get(slot_5)

        fifth_selection_l2mr1 = Marriage_Registration_l2_1.get(slot_5)
        fifth_selection_l2mr2 = Marriage_Registration_l2_2.get(slot_5)
        fifth_selection_l2mr3 = Marriage_Registration_l2_3.get(slot_5)
        fifth_selection_l2mr4 = Marriage_Registration_l2_4.get(slot_5)

        tn_fifth_selection_l2dr1  = tn_Document_Registration_l2_1.get(slot_5)
        tn_fifth_selection_l2dr2  = tn_Document_Registration_l2_2.get(slot_5)
        tn_fifth_selection_l2dr3  = tn_Document_Registration_l2_3.get(slot_5)
        tn_fifth_selection_l2dr4  = tn_Document_Registration_l2_4.get(slot_5)
        tn_fifth_selection_l2dr5  = tn_Document_Registration_l2_5.get(slot_5)
        tn_fifth_selection_l2dr6  = tn_Document_Registration_l2_6.get(slot_5)
        tn_fifth_selection_l2dr7  = tn_Document_Registration_l2_7.get(slot_5)
        tn_fifth_selection_l2dr8  = tn_Document_Registration_l2_8.get(slot_5)
        tn_fifth_selection_l2dr9  = tn_Document_Registration_l2_9.get(slot_5)
        tn_fifth_selection_l2dr10 = tn_Document_Registration_l2_10.get(slot_5)
        tn_fifth_selection_l2dr11 = tn_Document_Registration_l2_11.get(slot_5)
        tn_fifth_selection_l2dr12 = tn_Document_Registration_l2_12.get(slot_5)
        tn_fifth_selection_l2dr13 = tn_Document_Registration_l2_13.get(slot_5)
        tn_fifth_selection_l2dr14 = tn_Document_Registration_l2_14.get(slot_5)
        tn_fifth_selection_l2dr15 = tn_Document_Registration_l2_15.get(slot_5)
        tn_fifth_selection_l2dr16 = tn_Document_Registration_l2_16.get(slot_5)
        
        tn_fifth_selection_l2mr1 = tn_Marriage_Registration_l2_1.get(slot_5)
        tn_fifth_selection_l2mr2 = tn_Marriage_Registration_l2_2.get(slot_5)
        tn_fifth_selection_l2mr3 = tn_Marriage_Registration_l2_3.get(slot_5)
        tn_fifth_selection_l2mr4 = tn_Marriage_Registration_l2_4.get(slot_5)

        
        
        
        if (v == 'English'):

           
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_1':
                if slot_5 in list(Document_Registration_l2_1.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr1)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_2':
                if slot_5 in list(Document_Registration_l2_2.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr2)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_3':
                if slot_5 in list(Document_Registration_l2_3.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr3)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_4':
                if slot_5 in list(Document_Registration_l2_4.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr4)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_5':
                if slot_5 in list(Document_Registration_l2_5.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr5)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_6':
                if slot_5 in list(Document_Registration_l2_6.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr6)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_7':
                if slot_5 in list(Document_Registration_l2_7.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr7)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_8':
                if slot_5 in list(Document_Registration_l2_8.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr8)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_9':
                if slot_5 in list(Document_Registration_l2_9.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr9)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_10':
                if slot_5 in list(Document_Registration_l2_10.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr10)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_11':
                if slot_5 in list(Document_Registration_l2_11.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr11)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_12':
                if slot_5 in list(Document_Registration_l2_12.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr12)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_13':
                if slot_5 in list(Document_Registration_l2_13.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr13)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_14':
                if slot_5 in list(Document_Registration_l2_14.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr14)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_15':
                if slot_5 in list(Document_Registration_l2_15.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr15)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_en_Document_Registration_l2_16':
                if slot_5 in list(Document_Registration_l2_15.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2dr16)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}


            if z== 'utter_ask_2nd_layer_en_Marriage_Registration_l2_1':
                if slot_5 in list(Marriage_Registration_l2_1.keys()):
                    if slot_5 == '5':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2mr1)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            elif z== 'utter_ask_2nd_layer_en_Marriage_Registration_l2_2':
                if slot_5 in list(Marriage_Registration_l2_1.keys()):
                    if slot_5 == '5':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2mr2)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            elif z== 'utter_ask_2nd_layer_en_Marriage_Registration_l2_3':
                if slot_5 in list(Marriage_Registration_l2_1.keys()):
                    if slot_5 == '7':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = fifth_selection_l2mr3)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            elif z== 'utter_ask_2nd_layer_en_Marriage_Registration_l2_4':
                if slot_5 in list(Marriage_Registration_l2_1.keys()):
                    if slot_5 == '4':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}

                    else:
                        dispatcher.utter_message(text = fifth_selection_l2mr4)
                        y = None

                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}


        if (v=='Tamil'):

            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_1':
                if slot_5 in list(tn_Document_Registration_l2_1.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr1)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_2':
                if slot_5 in list(tn_Document_Registration_l2_2.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr2)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_3':
                if slot_5 in list(tn_Document_Registration_l2_3.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr3)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_4':
                if slot_5 in list(tn_Document_Registration_l2_4.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr4)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_5':
                if slot_5 in list(tn_Document_Registration_l2_5.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr5)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_6':
                if slot_5 in list(tn_Document_Registration_l2_6.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr6)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_7':
                if slot_5 in list(tn_Document_Registration_l2_7.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr7)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_8':
                if slot_5 in list(tn_Document_Registration_l2_8.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr8)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_9':
                if slot_5 in list(tn_Document_Registration_l2_9.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr9)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_10':
                if slot_5 in list(tn_Document_Registration_l2_10.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr10)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_11':
                if slot_5 in list(tn_Document_Registration_l2_11.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr11)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_12':
                if slot_5 in list(tn_Document_Registration_l2_12.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr12)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_13':
                if slot_5 in list(tn_Document_Registration_l2_13.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr13)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_14':
                if slot_5 in list(tn_Document_Registration_l2_14.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr14)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_15':
                if slot_5 in list(tn_Document_Registration_l2_15.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr15)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            if z == 'utter_ask_2nd_layer_tn_Document_Registration_l2_16':
                if slot_5 in list(tn_Document_Registration_l2_16.keys()):
                    if slot_5 == '2':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2dr16)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}


            if z== 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_1':
                if slot_5 in list(tn_Marriage_Registration_l2_1.keys()):
                    if slot_5 == '5':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2mr1)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            elif z== 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_2':
                if slot_5 in list(tn_Marriage_Registration_l2_1.keys()):
                    if slot_5 == '5':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2mr2)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            elif z== 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_3':
                if slot_5 in list(tn_Marriage_Registration_l2_1.keys()):
                    if slot_5 == '7':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}
                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2mr3)
                        y = None
                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}
            elif z== 'utter_ask_2nd_layer_tn_Marriage_Registration_l2_4':
                if slot_5 in list(tn_Marriage_Registration_l2_1.keys()):
                    if slot_5 == '4':
                        dispatcher.utter_message(response = 'utter_lang_selection' )
                        y = None
                        return {"choices_1": None,"choices_2": None,"choices_3": None,"choices_4": None,"choices_5": None}

                    else:
                        dispatcher.utter_message(text = tn_fifth_selection_l2mr4)
                        y = None

                        time.sleep(3)
                else:
                    dispatcher.utter_message(response = "utter_ask_valid_responce")
                    return {"choices_5": None}


        return {"choices_5": slot_value}

class ActionResetLoop(Action):
    def name(self) -> Text:
        return "action_reset_loop"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [Restarted(), AllSlotsReset()]



class ActionCheckInputValidity(Action):
    def name(self):
        return "action_check_input_validity"

    def run(self, dispatcher, tracker, domain):
        if tracker.latest_message['intent'].get('name') != 'first_layer':
            dispatcher.utter_message(response= "utter_ask_start_valid_response")
            return [UserUtteranceReverted()]
        else:
            return []




    

    


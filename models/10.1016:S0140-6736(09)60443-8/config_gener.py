#The purpose of this script is to create a starting place for generating a 
#config file that allows us to reassemble a model and its environment
#import pprint
#pp = pprint.PrettyPrinter(indent=4)

config = {}

config['model_name'] = 'Development of a Risk Score for Atrial Fibrillation in the Community'
config['model_category'] = ['prognostic'] #choices: 'diagnostic','prognostic'
config['predictive_ability'] = {}
config['predictive_ability']['type'] = [] #choices: 'apparent_performance','internal_validation','non-random_split','random-split','external_validation'
config['predictive_ability']['metric'] = []
config['predictive_ability']['value'] = []
config['predictive_ability']['lcl'] = []
config['predictive_ability']['ucl'] = []
config['target_population'] = 'C0001675' #NCI Metathesaurus CUI
config['outcome'] = 'C3176364' #NCI Metathesaurus CUI
config['predictors'] = {}
config['predictors']['function_inputs'] = ['Sex (Male = True)','Age','Body Mass Index','Sbd (Systolic Blood Pressure)','Antihypertensive Medication Use','Pr Interval (Seconds)','Valvular Heart Disease (Significant Murmur)','Prevalent Heart Failure'] #named parameters in the submitted function
config['predictors']['cuis'] = ['C28421','C080440','C1542867','C048805','C068416','C0488345','C1963123','C0018801'
] #mapping to NCI Metathesaurus CUI's
config['predictors']['labels'] = ['Categorical','Quantitative','Quantitative','Quantitative','Categorical','Quantitative','Categorical','Categorical'] #labels that would be helpful to elicit responses from humans
config['model_env_requirements_file'] = '' #name of a requirements file that determines how to recreate model environment
config['model_development_data'] = {}
config['model_development_data']['sample_size'] = '4764'
config['model_development_data']['missing_data_strategy'] = ''
config['model_object'] = {}
config['model_object']['file_name'] = '' #name of model object file
config['model_object']['object_name'] = '' #name of the model as stored as an object (where that's a function or a module package model object)
config['model_object']['language'] = 'python' #currently only supports python, R

import json
with open('config.json','w') as output:
    json.dump(config,output)

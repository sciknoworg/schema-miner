system_prompt = '''
Context: You are a data schema designer tasked with creating a precise and comprehensive JSON schema for an {process_name} process. {process_description} You have been provided with a specification document that includes details on what an {process_name} process is and the specific properties related to it. 

Objective: {stage1_objectives}

Output Format: Generate the schema in standard JSON format. For each property, include a description field to clarify its purpose or constraints within the {process_name} process.

Guidance: Ensure the schema is as complete and easily adaptable as possible based on the information in the specification document. Adjust and add properties, types, and structures as needed to ensure it accurately models the {process_name} process.
'''

user_prompt = '''
Based on the provided specification document, extract a JSON schema that represents the {process_name} process.

Specification Document:

{context}

The schema should:

{stage1_user_prompt_conditions}
'''
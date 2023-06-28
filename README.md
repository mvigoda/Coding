# ChatGPT use cases for Physicians  

**Obviously Chat GPT should not replace clinical expertise or judgment, but**



> Legend:
>
> - 🟥: Not implemented
> - 🟨: Legacy material available, to be updated or re-written
> - 🟦: Available, modification required
> - 🟩: Good to go





### Use Cases 

Description | Link | Overview | Assigned To | Status
:---:|:-----:|:------------:|:-----------:|:-----------:
`Synopsis of Multiple Clinic Notes`| [Oncology](https://github.com/mvigoda/Coding/blob/master/Cancer_Patient_Synopsis.ipynb) | [Synopsis of Multiple Clinic Notes](#synopsis-of-multiple-clinic-notes) | Philip | 🟨
`Preventive Care Recommendations`| [PCP](https://github.com/mvigoda/Coding/blob/master/Infer_Preventive_Health_Recommendations.ipynb) | [PCP Annual Visit](#pcp-annual-visit---and-preventive-care-recommendations) | TBC | 🟨
`Clinic Scheduling`| [_Administrative_](https://github.com/UCL-DSS/matplotlib-workshop) | Basic Python | TBC | 🟨
`Extract Lab Values`| [_Git_ and _GitHub_](https://github.com/UCL-DSS/git-workshop) | None | Philip | 🟩
`TK05`| [_SQL_](https://github.com/UCL-DSS/SQL_workshop) | None | Philip | 🟩









Chat GPT can be helpful for physicians reviewing clinical records in several ways:

### Efficient Data Extraction   
  Chat GPT can assist in automatically extracting relevant data points, such as:
 
- Patient Demographics
- Medical History
- Medications
- Lab Results
- Diagnoses  
    

In this manner, it can be used to **analyze text and generate structured summaries**.

### Decision Support  
- Analyzing clinical records and offering insights based on patterns, guidelines, and previous similar cases. 
- Identify potential drug interactions
- Flag abnormal test results  
- Suggest further diagnostic tests or treatment options  
- Provide evidence-based recommendations  

### Documentation Assistance  
- Aid in generating accurate and comprehensive clinical notes by analyzing the clinical records and providing suggestions for relevant information to include
- Help with formatting, grammar, and terminology consistency, resulting in more efficient and standardized documentation.

### Natural Language Interface  
- Ask questions in plain language, such as "What was the patient's blood pressure during the last visit?" or "Has the patient reported any allergies?"
- Interpret these queries, search the clinical records, and provide relevant answers, saving time and improving accessibility to patient information.






<a id="synopsis-of-multiple-clinic-notes"></a>
## Synopsis of Multiple Clinic Notes  

Some Markdown text with <span style="color:red">some *red* text</span>.

<div class="alert alert-block alert-danger">
description goes here
</div>

 


A number of use cases are considered where chatGPT may prove useful for clinicians:
1. [Cancer Patient Synopsis of Multiple Clinic Notes](https://github.com/mvigoda/Coding/blob/master/Cancer_Patient_Synopsis.ipynb)
	- Multiple clinic notes for the same patient 
	- Organize them in chronological order
	- Extract relevant data from each visit to provide a synopsis
2. [PCP Annual Visit - and Preventive Care Recommendations](https://github.com/mvigoda/Coding/blob/master/Infer_Preventive_Health_Recommendations.ipynb)

Other use cases can be considered administrative:
1. A patient has a medical concern and is interested in finding out when a particular is open.

<a id="pcp-annual-visit---and-preventive-care-recommendations"></a>
## PCP Annual Visit - and Preventive Care Recommendations

The following code uses the chatGPT API and performs the following :
1. Read a clinic note
2. Identify Medical Considerations based on Clinical Note
	- Determine 5-7 medical considerations (one or two words in length) 
3. Create Assessment and Plan
	- Include relevant preventive health recommendations
4. Identify the MEDICATIONS - and the relevant MEDICAL CONDITIONS
5. Highlight the MEDICATIONS in the note
6. Preventive Care Recommendations - as Written by Physician  
	- Extract relevant information to form recommendations regarding preventive healthcare.
	- 3-5 areas appropriate for the patient described in the clinical note.
7. Preventive Care Recommendations - Personalized for the Patient

```Preventive Health Recommendations

1. Smoking cessation: Maria, quitting smoking is one of the best things you can do for your health. I recommend calling Kick it California at 1-800-300-8086 to get started on your journey to a smoke-free life.

2. Cardiovascular disease prevention: Given your family history of cardiovascular disease, it's important to take steps to prevent it. I recommend incorporating more heart-healthy foods into your diet, such as fruits, vegetables, and whole grains. Additionally, regular exercise can help keep your heart healthy.

3. Cancer screening: Maria, given your mother's history of colon cancer, it's important to stay up to date on your cancer screenings. I recommend scheduling a colonoscopy with your primary care physician to ensure that you are in good health.

4. Osteoporosis prevention: As a woman over the age of 50, you are at an increased risk for osteoporosis. I recommend incorporating weight-bearing exercises into your routine, such as walking or lifting weights, to help keep your bones strong. Additionally, make sure you are getting enough calcium and vitamin D in your diet.

5. Immunizations: It's important to stay up to date on your immunizations to prevent illness. I recommend getting a flu shot every year and discussing other recommended vaccines with your primary care physician.
```

7. Show Specific Reasons for Recommendations
	- Medical Consideration
    	- Recommendation
    	- Reason for Recommendation

```Preventive Health Recommendations

1. Cardiovascular Disease Prevention
    a. The patient reports a family history of cardiovascular disease, with her father having a heart attack in his late 60s.
    b. Medical History: The patient has a history of hypertension and hyperlipidemia, both of which are well-managed with medications.
    c. Assessment and Plan: Recommend regular cardiovascular screening, including blood pressure and cholesterol checks, as well as lifestyle modifications such as smoking cessation and regular exercise.

2. Cancer Screening
    a. Family History: The patient's mother had colon cancer but is currently in remission.
    b. Assessment and Plan: Recommend regular colon cancer screening, such as colonoscopy, as well as breast cancer screening, such as mammography.

3. Smoking Cessation
    a. Social History: The patient smokes 1/2 ppd.
    b. Assessment and Plan: Recommend smoking cessation interventions, such as nicotine replacement therapy or counseling, to reduce the risk of lung cancer and other smoking-related illnesses.
```

The notes are seen here:

![alt text](patient_notes.png "Here is Title")

In the second note, we have highlighted the medications that are referenced in the note, as well as the ANC and HCT values.

![alt text](patient_notes_1.png "Here is Title")



 

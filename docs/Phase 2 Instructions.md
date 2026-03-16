Project part 2 is about working from the prior phase to try new ideas (of your choice). This can include trying entirely new methods/techniques or improving on some of what you did in phase 1\.

Phase 1 is graded using an autograder and contributes up to 12 points. Your autograder grade is added to the below scores for phase 2 to calculate your overall final project grade. Each of the items in the below rubric are expanded upon in their own sub-section below the table.

| Category | Well Beyond Expectations (4.5pts) | Excellent (4pts) | Good (3pts) | Approaching (2pts) | Learning (1pts) | Missing (0pts) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Scope | Scope is at least 1 above what was required and all extensions achieve some results | Scope is as required by group size. At least 70% of scope items (rounded up) achieve some results (the remaining had an effect, but their value was debatable) | At least 40% of scope items (rounded up) achieve some results (the remaining had an effect, but their value was debatable). Grade may also be due to scope penalty | At least 25% of scope items (rounded up) achieve some results (the remaining had an effect, but their value was debatable). Grade may also be due to scope penalty | All scope items had an effect, but their value was debatable. Grade may also be due to scope penalty | Can only be achieved due to scope penalties (possibly in combination with deductions for lack of value) or if not submitted by the deadline |
| Report | All elements of “excellent” plus shows significant insight about each technique applied beyond what is expected/required. Must not have received any scope penalties | Write-up is clear, well organized, contains a bibliography, and involves all group members to a reasonable degree. Solid understanding of concepts utilized and their impact is displayed. Must have at least a 2 in scope | The project is lacking in 1 of the aforementioned aspects. Must have at least 1 in scope | The project is lacking in 3 of the aforementioned aspects. | The project is lacking in all of the aforementioned aspects. | The project report was not submitted by the deadline |
| Reflection | N/A | Reflection shows significant consideration and offers meaningful insight as to the students experience with the project (highlighting some positive and negative elements of the experience) | Reflection shows some consideration and offers some insight as to the students experience with the project | Reflection shows little consideration **or** offers no insight as to the students experience with the project | Reflection shows little consideration **and** offers no insight as to the students experience with the project | The project reflection was omitted or phase 2 as a whole was not submitted |

---

<ins>**Full Details Phase 2 Details by Item**</ins>


<ins>**Scope**</ins>

You are expected to make a certain number of additions to phase 1 of the project based on group size. Note that these are **additions** and thus, they must be applied on top of the techniques applied in phase to net additional improvements (not in place of them). The options for extensions are outlined in full at the end of this section, though you may reach out to staff for approval and point allocation to ideas of your own.  
Someone working alone must do 4 points of the below. A team working as a pair must do 7 points of the below. A project will lose 1 point from the “phase 2 scope” portion of the rubric per missed point of scope. If an item from the below appears to have little to no impact on results or was significantly incorrectly implemented, it may not be counted towards scope. If it was reasonably implemented and had some impact, but it is not entirely clear if that impact is positive or has any value, then this item may be counted as a “partially successful.” The rubric explains what percentage of “partial successes” can lead to what deduction, but here is the list with numbers by group size instead of percentages (assuming 4 scope points for solo work and 7 for a pair of students):

Solo: \-1 for 2/4 partial successes, \-2 for 3/4 partial successes, \-3 for 4/4 partial successes

Duo: \-1 for 3/7 partial successes, \-2 for 5/7 partial successes, \-3 for 7/7 partial successes

Your implementation of the below need not yield vast improvements in results, but must have some recognizable positive impact in a non-negligable number of cases to be counted as fully successful. Any results then **must** be highlighted in your report. Scope penalties can have an impact on the report (as they inherently limit what you write about in your report), but to a lesser degree (see the table above).  We reserve the right to increase the scope contribution of any of the below

Points in the below list reflect the scope contribution of that item. Extension items that do not require pre-approval include:

* Use the full data set rather than the \~10% used in the first phase (1 point)  
* Reduced dataset dimensionality via feature selection (1 point)  
  * This is not a method in and of itself, but an idea one can add onto another approach (including those from phase 1\) for improved results and a extra point)  
* Any other additional forms of ensemble learning  
  * Section 19.8  
    * 19.8.3 \- Stacking (2 point)  
    * 19.8.6 \- Online learning (3 points, for this one would need to simulate the online case by having “base” data and new data provided over time)  
    * As an alternative, you may try to “fuse” your random forest and gradient boosting methods for improved results compared to either independently (1 point)  
* Model uncertainty by learning a probabilistic model  
  * Chapter 20 (must read 20.1)  
    * 20.2.7 \- Learning Bayes net structure (4 points)  
      * 20.3.2 \- Learning Bayes net parameter values for hidden variables (+2 point, for adding a reasonable hidden variable and incorporating into the bayes net learning)  
* Simulate RL application  
  * We want to allocate resources to improve student performance. Build an MDP with rewards based on allocation of resources and results of this, then use active RL to learn the action utility function (see 22.3) or an optimal policy (see 22.5) for intervention and resource allocation (4 points)  
    * Use any of the generalizations/estimation methods from 22.4 (+2 points)  
* Neural Networks (4 points for one, 7 points for 2 distinct families and comparison)  
  * Section 21.6 \- Recurrent Neural Network (RNN)  
  * Section 24.4 \- Transformers




<ins>**Report**</ins>

This should include an overview of the work, sections for each element from scope that was incorporated, a reflection (scored separately, see below) and a full bibliography. The sections on each scope element should include some details as to what that technique is, how it was implemented to address the given problem, and the results (with tables/figures as appropriate). There is no specific page minimum or limit, but I will say that the focus is primarily upon quality, not quantity. Focus on demonstrating a basic understanding of the topic, its contextual relevance to the problem, and clearly expressing your results and their degree of significance, **not** on length. For example, 1 to 2 good pages of text on a sub-topic plus supporting data in tables/graphs would be sufficient.  
The report must be typed, but need not be done in LaTeX. If you choose not to use LaTeX, your mathematical content must be similarly well type-set as it would be had you used LaTeX, so be aware that you will either need to grapple with the general pain of LaTeX use or with the sometimes extremely difficult battle of trying to wrestle clean mathematical equations out of something like Microsoft Word. Which will be easier to use depends heavily on the nature of your project and will also depend somewhat on your group’s comfort level with LaTeX.  
Please note that, as with other assessments, you may **not** use LLMs to generate non-negligible ideas or content included in your project and must understand all content you include in your project.  
For groups of 2, a single report for both group members is submitted.

<ins>**Reflection**</ins> 

This should be included in your report, but has its own distinct rubric items. You should give a 1 to 2 paragraph answer to each of the following questions in your reflection:

* What was your favorite part of the project?  
* What was your least favorite part of the project?  
* On what topic from the course did your perspective change the most from before to after the project? Did your opinion of the usefulness of this topic go up or down after working with it within the context of the project?  
* If you had more time, which scope item (or item from phase 1\) that you implemented would you wish to improve the implementation of further and how might you try to do this?  
* If you had more time, what new scope item/ techniques would you like to try to apply and why?  
* Any recommendations to improve the project experience for future students? (optional)  
* Roughly how many hours did you spend one phase 1 and phase 2 of the project respectively? This can be a 1 sentences answer and will **not** impact grade (optional)

While we expect thoughtful engagement for the reflection portion of the project and answers of non-negligible length/content, it is still probably the area of the project with the most favorable effort-to-points ratio for students. We are not setting an unreasonably high bar to receive 4 points on the reflection, so please do not skimp on it and lose points unnecessarily here. Give each question some consideration and a 1 to 2 paragraph answer that reflects some thought. You **may** use an LLM here to assist yourself with English-language expression of what you wish to say, but you may **not** use an LLM here to generate ideas for how you should answer these questions (I want **your** reflection, not the LLMs fever dream about a project it doesn’t understand). That being said, I understand the value of tools like Grammarly for working on complex personal expression.  
	For groups of 2, a single reflection is submitted. Group members can either submit a single answer to each question that reflects their joint opinion, or both members may have a short answer for each question. It is allowed (but not required) to note which opinions belong to which group member.

<ins>**Extra Credit**</ins> 

While we set a high bar for full credit on the final project, we do not wish the standard for such to be unreasonable. In addition, there is occasionally a student or group that decides to go above and beyond in one or more ways on a project. Thus, we wish to leave some room to acknowledge such efforts (while still allowing other solid projects to achieve full or high marks). Thus, we reserve the right to give 4.5 out of 4 in one of the several categories that went significantly beyond our expectations in one or more ways. Most projects will not receive any extra credit. Further, we wish to highlight that this is **not** the most efficient way to improve your grade. Thus, we strongly discourage students from letting the pursuit of extra credit on one rubric item get in the way of completing other rubric items (as this is likely to negatively impact your overall score).  

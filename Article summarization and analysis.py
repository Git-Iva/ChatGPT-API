import openai
from keys import API_Key
openai.api_key  = (API_Key)

def get_completion(prompt, model="gpt-3.5-turbo"): 
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # indicates the randomness of the model's output. Since it's a summary, I don't want any randomness and creativity
    )
    return response.choices[0].message["content"]

# The article was published in the Guardian on 4 May 2023
# Author: Sofia Quaglia

article = """

Title: Melting glaciers in Alps threaten biodiversity of invertebrates, says study
Invertebrates living in the cool meltwater rivers of the European Alps could lose most of their habitat and disappear, as the mountain range’s glaciers melt at an unprecedented rate due to climate change, according to a study.
Although they are often overlooked, these animals are crucial for alpine ecosystems.
Researchers focused on the mountain range of the Alps and collated data from 30 years of studies on the rate at which its glaciers are melting, and how that affects the area’s river flows over time. They homed in on how past changes affected the populations of 15 species of invertebrates such as midges and stoneflies that are specialised at living in those waters.
Some species of mayflies are sometimes known as blue-winged olive flies by people who do fly-fishing. Midges tend to be mistaken for mosquitoes and are also known as lake flies. Glacier-fed rivers are generally species-poor, as few species can cope with this environment, so these creatures are quite adaptive and specialised to hostile environments.
Using the data, the researchers were able to make a prediction of how these species will fare between now and 2100.
As global heating causes a big decrease in the glacier cover of the Alps, rivers will become drier and flow slower, sometimes disappearing, according to Lee Brown, a professor of aquatic science at the University of Leeds and one of the lead authors of the study.
Water will become warmer as it will no longer be chilled by the melting ice, becoming inhospitable to invertebrates that have evolved to thrive in cold, unstable and nutrient-poor conditions. “The habitat for those specialist species is shrinking rapidly,” said Brown.
Most of the species will face population drops, and the stonefly Rhabdiopteryx and three species of non-biting midges will face the risk of extinction in the Alps.
“These small animals represent unique biodiversity and genetic diversity,” said Dean Jacobsen, an associate professor of freshwater biology at the University of Copenhagen, who was not involved in the study. “They are often overlooked because they are small and not particularly charismatic. But they form part of food webs and conduct vital ecosystem processes like organic matter breakdown and transformation.” They are also food for fish, birds, and mammals in water and on land.
The broader ecological consequences are difficult to foresee if the species are lost or replaced by other species, according to Jacobsen. The calculations do not take into account that the environmental requirements of species may change over time, and they may adapt to new conditions.
The models suggest that some species may be able to find refuge in areas where the climate is less hostile for them. “There might be little pockets of ice that remain in some of the really high parts of the Alps where the species can hang on,” Brown said.
Yet many of these plausible havens are also potential hotspots for development or tourism and could disappear before these species get there.
Plus, it is unclear whether these invertebrates have the ability to migrate to these new environments anyway. Previous research has shown that they are not very good at moving from one river to another or flying long distances.
There is now discussion about possible operations to collect some of these invertebrates and transfer them to places where they can establish populations.
“It’s a bit more hands-on conservation work, we don’t tend to do it much for insects and other invertebrates,” said Brown. “But we do it for fish, and we did for some big carnivores like wolves and beavers. So maybe we should be doing it for insects.

"""

prompt = f""" Your task is to generate a summary of this article below delimited by triple backticks. Use 30 words at most.
            Then answer the following questions and format your response like this:
         1. Produce summary (Summary:)
           
         2. Identify sentiment - positive or negative (Sentiment: )

         3. Is the author expressing fear (Expressed fear: yes or no)

         2. Spieces facing extinction (Endangered: list names of spieces only, separated by comma. Don't use a full sentence)

         3. Possibe solutions (List solutions only, separated by commas. Don't use a full sentence)

         4. List the names of all researchers you can identify (Studies by: list reseacher name (title), list researcher name (title))
       

         Article: ```{article}```
"""
response = get_completion(prompt)
print(response)


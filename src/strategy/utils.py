# Utils for the strategies

def construct_prompt(entity: str, type_: str, lang: str = 'en') -> str:
    """
        A utility function responsible for prompt construction
        Parameters:
            entity (string): The entity to construct the prompt for
            type_ (string): The type of the entity (job or skill)
            lang (string): The language in which the prompt is constructed
        Returns:
            prompt (string): The prompt to send to the API
    """
    prompt = ""
    if lang == 'en':
        if type_ == 'job':
            prompt = f"Give a detailed description about this job {entity}, skills, tools,missions and tasks and pretty much every thing about it"
        else:
            # skill
            prompt = f"Give a detailed description about this skill {entity}, jobs that could be used in and pretty much every thing about it"

    if lang == 'fr':
        if type_ == 'job':
            prompt = f"Donnez une description détaillée de cet emploi {entity}, des compétences, des outils, des missions et des tâches et de pratiquement tout ce qui s'y rapporte."
        else:
            # skill
            prompt = f"Donnez une description détaillée de cette compétence {entity}, des emplois dans lesquels elle peut être utilisée et d'à peu près tout ce qui s'y rapporte."

    return prompt

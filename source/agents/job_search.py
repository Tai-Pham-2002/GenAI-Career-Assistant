from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchResults
from langchain_ollama import ChatOllama
from utils import save_file, show_md_file

class JobSearch:
    def __init__(self, prompt):
        self.model = ChatOllama(model="qwen3:4b", temperature=0.0, num_gpu=100)
        self.prompt = prompt
        self.tools = DuckDuckGoSearchResults()

    def find_jobs(self, user_input):
        results = self.tools.invoke(user_input)
        chain = self.prompt | self.model
        jobs = chain.invoke({"result": results}).content
        print(jobs)
        path = save_file(str(jobs).replace("```markdown", "").strip(), 'Job_search')
        print(f"Jobs saved to {path}")
        return path
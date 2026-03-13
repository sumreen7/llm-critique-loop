from agents.writer import writer
from agents.critic import critic
from agents.editor import editor
from agents.judge import judge

MAX_ITERATIONS = 6

def run_agents(task):

    draft = writer(task)

    for i in range(MAX_ITERATIONS):

        critique = critic(task, draft)

        draft = editor(task, draft, critique)

        verdict = judge(task, draft)

        print("Iteration:", i + 1)
        print("Judge:", verdict)

        if verdict["approved"]:
            break

    return draft
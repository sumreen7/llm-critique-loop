from generator import generate_answer
from critic import critique_answer

MAX_ITERATIONS = 5


def run_loop(prompt):

    answer = generate_answer(prompt)

    history = []

    for i in range(MAX_ITERATIONS):

        critique = critique_answer(prompt, answer)

        history.append({
            "iteration": i+1,
            "answer": answer,
            "critique": critique
        })

        if "approve" in critique.lower():
            break

        revision_prompt = f"""
Original task:
{prompt}

Previous answer:
{answer}

Critique:
{critique}

Improve the answer.
"""

        answer = generate_answer(revision_prompt)

    return answer
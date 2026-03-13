from generator import generate_answer
from critic import critique_answer

MAX_ITERATIONS = 5


def run_loop(prompt):

    answer = generate_answer(prompt)

    for i in range(MAX_ITERATIONS):

        print(f"\nIteration {i+1}")

        critique = critique_answer(prompt, answer)

        print("Claude critique:", critique)

        if "approve" in critique.lower():
            print("Approved by Claude")
            return answer

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
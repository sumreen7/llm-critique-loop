from agents.writer import writer
from agents.critic import critic
from agents.editor import editor
from agents.judge import judge

MAX_ITERATIONS = 6

def run_agents(task):
    # Parse JD and RESUME from structured input
    if "RESUME:" in task and "JD:" in task:
        parts = task.split("RESUME:", 1)
        jd = parts[0].replace("JD:", "").strip()
        original_resume = parts[1].strip()
    else:
        jd = task
        original_resume = task

    history = []

    print("\n=== WRITER: Generating initial draft ===")
    draft = writer(jd, original_resume)

    for i in range(MAX_ITERATIONS):
        print(f"\n=== ITERATION {i+1} ===")

        critique = critic(jd, original_resume, draft)
        score = critique.get("score", 0)
        approved = critique.get("approved", False)
        lang_score = critique.get("language_alignment_score", 0)
        qual_score = critique.get("quality_score", 0)

        print(f"Score: {score}/10 | Language: {lang_score}/10 | Quality: {qual_score}/10")
        print(f"Issues: {len(critique.get('issues', []))}")
        print(f"Feedback: {critique.get('overall_feedback', '')[:300]}")

        history.append({
            "iteration": i + 1,
            "score": score,
            "language_alignment_score": lang_score,
            "quality_score": qual_score,
            "issues_count": len(critique.get("issues", [])),
            "feedback": critique.get("overall_feedback", ""),
            "missing_keywords": critique.get("missing_jd_keywords", [])
        })

        if approved:
            print("\n=== CRITIC APPROVED — Running final judge ===")
            verdict = judge(jd, original_resume, draft)
            print(f"Judge: {verdict}")
            if verdict.get("approved"):
                print("=== JUDGE APPROVED. DONE. ===")
                break
            else:
                print(f"Judge rejected: {verdict.get('reason')}")

        print("\n=== EDITOR: Applying fixes ===")
        draft = editor(jd, original_resume, draft, critique)

    return draft, history
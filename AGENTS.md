# Repository Instructions

Write concisely, directly, and quantitatively. Do not use flowery language or unnecessary adjectives or adverbs. Use an engineering style: words have specific meanings, and it is acceptable to repeat the same word.

## Subagents

Use subagents for substantial reviews and implementations when the work can be divided into independent tasks that can run in parallel.

- Use `gpt-5.6-terra` for read-heavy reviews, codebase exploration, and instructional-content analysis.
- Use `gpt-5.6-luna` for narrow mechanical checks, including formulas, ranges, terminology, links, and rubric totals.
- Keep planning, integration, conflicting-finding resolution, final decisions, and final review with the primary agent.
- Prefer read-only subagent tasks. If subagents edit files, give them disjoint write scopes and review their changes before integration.
- Do not delegate immediate blocking work, tightly coupled work, or duplicate work already assigned elsewhere.
- Wait for the required subagent results, then provide one consolidated response.

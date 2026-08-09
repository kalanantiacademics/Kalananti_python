# Kalananti B2C Python Program — Deck & Lesson Plan Generation Rules

You are an agent assisting with Kalananti's B2C Python programming materials. These rules are mandatory whenever creating, reviewing, or updating a student deck or teacher-facing lesson plan.

## 1. Mandatory Preflight — Read Before Doing Anything

Before planning, editing, or generating any material, you MUST:

1. Read this `AGENTS.md` completely.
2. Read `syllabus_python_kalananti.md` completely and locate the requested `level_id` and `session_order`.
3. When internet access is available, validate the local syllabus against the Google Sheet below, tab `B2C_Python`:
   `https://docs.google.com/spreadsheets/d/1nbaaeUrlCb_BUJwdVKovwNy0RGmkspYOfzK9CZLy7cM/edit?usp=sharing`
4. Read the relevant previous session so the review, terminology, examples, and difficulty are continuous.
5. For Meeting 1, inspect the previous level. For Level 1 Meeting 1, use the Trial Class/Level 0 as the prior-learning reference; if students did not attend Trial Class, use a five-slide diagnostic warm-up instead.
6. Inspect the established deck implementations in `level1/`, `level2/`, and `level3/` before creating a new level or changing shared visual/interaction patterns.
7. Inspect every example in `level/source-code/` for the requested level, when available, to understand possible personal-project outcomes.
8. Confirm the requested artifact type before writing. A student deck and a teacher-facing lesson plan are separate artifacts. Teacher notes, facilitator scripts, preparation guidance, answer reasoning, and detailed teaching-time allocations MUST NOT be inserted into a student deck; create them only in a separately requested lesson-plan artifact.

Do not start creating content from memory before completing this preflight.

## 2. Source Priority and Conflict Handling

Use this priority order:

1. The user's explicit request.
2. `syllabus_python_kalananti.md` as the local curriculum source of truth.
3. The Google Sheet `B2C_Python` as the latest validation reference.
4. `level/source-code/` as inspiration for achievable personal/final-project outcomes.
5. Existing Level 1–3 decks as visual, UX, and interaction references.

The program structure is:

- Level 0: Trial Class only.
- Levels 1–6: six main program levels.
- Every main level contains exactly 12 meetings.

If sources disagree, do not silently merge or invent a compromise. Preserve the syllabus topic/library and report the mismatch. Source-code examples NEVER override the syllabus.

Known examples may use a different technology from the current syllabus, such as Pygame instead of Arcade or Flask instead of Streamlit. Treat their product idea and feature scope as inspiration, but adapt the implementation to the library named by the syllabus. Arcade and Pygame are separate Python libraries.

Do not add a required concept merely because it appears in an example project. Every required project feature must be traceable to Meetings 1–8 of the same level. Features beyond the syllabus may only appear as clearly labeled optional bonus challenges with sufficient starter support.

## 3. Artifact Scope and File Structure

- The deck is displayed directly to students. Use student-facing language and instructions.
- Do not embed teacher-only notes, teacher scripts, classroom-management directions, or lesson-plan tables in the deck.
- Lesson plans will be created separately when explicitly requested.
- Each level should have one main `deck.html` containing exactly 12 meeting tabs, unless the user requests a different structure.
- Preserve unrelated files and existing user changes.
- Reuse established components and assets instead of duplicating navigation or interaction code per slide.

## 4. Lesson Plan Artifacts — Teacher-Facing Standard

Lesson plans are separate teacher-facing artifacts. Create or update them only when the user explicitly requests a lesson plan, learning plan, facilitator guide, or teacher preparation document. A lesson plan is read before and during teaching; it must help the teacher understand the material, prepare the environment, anticipate student difficulties, and deliver every deck activity confidently.

### A. Purpose and Audience

- Write for the teacher or instructor, not for students and not for curriculum developers.
- Use clear Bahasa Indonesia while preserving original English programming terms and defining them accurately.
- The teacher must not need to reverse-engineer the student deck, source code, or syllabus to understand what to teach.
- Expand explanations that are intentionally brief in the student deck. The lesson plan should contain the missing teaching context, technical reasoning, expected behavior, and facilitation notes.
- Do not copy student-facing slide text without adding teacher value.
- Do not insert internal audit content such as source-priority tables, repository paths, validation status, implementation notes, “scope and source alignment,” or statements about which source was used. Report source conflicts to the user separately, not inside the teacher document.
- Do not include developer-facing UI, debug controls, deck-generation notes, or repository maintenance instructions.

### B. Mandatory Lesson-Plan Preflight

Before writing a lesson plan, complete the same curriculum preflight required for decks, then also:

1. Read the full requested deck and map every meeting, section, activity, exercise, code sample, project checkpoint, and closing item.
2. Identify anything the deck assumes but does not explain sufficiently for a teacher: prerequisite concepts, setup steps, code behavior, expected output, common errors, vocabulary, activity transitions, and assessment evidence.
3. Syntax-check and, when practical, run every code example or reference implementation used for teacher explanation.
4. Inspect the preceding meeting and write the exact prior knowledge students should bring into the current meeting.
5. Inspect source-code gallery examples for achievable project outcomes, but label any concept outside Meetings 1–8 as optional teacher reference rather than a student requirement.
6. Confirm the intended meeting duration. If the user does not specify it, state the duration assumption in the handoff and keep the timing internally consistent.

### C. Required Front Matter

A complete level lesson plan should begin with teacher-useful information only:

- program/level name, planet theme, primary technology, audience, number of meetings, and assumed duration;
- concise course summary and end-of-level student outcome;
- prior-learning requirements from the previous level;
- student preparation and teacher preparation checklists;
- software, extensions, libraries, local assets, starter files, and hardware requirements;
- installation and verification commands when relevant;
- offline contingency and backup materials;
- learning journey table for all 12 meetings;
- project outcome examples and boundaries explained in teacher language;
- consistent debugging routine and differentiation approach.

The cover must use the correct local Kalananti logo, keep the original logo colors and aspect ratio, and remain readable when printed. Avoid decorative filters that make the logo illegible. Do not put “PDF ready,” “teacher-facing,” repository metadata, or other production labels on the cover unless the user asks for them.

### D. Required Structure for Every Meeting

Every meeting entry must be self-contained and include:

1. Meeting number, unit, topic, mastery focus, and assumed duration.
2. Observable learning objectives derived from the syllabus and deck.
3. Exact prior knowledge students should already know.
4. Student preparation: files, concepts, accounts, tools, and unfinished work they must bring.
5. Teacher preparation: software checks, packages, demo files, expected screenshots/output, deck section to open, and backup plan.
6. Materials and environment for both online and offline delivery.
7. Key vocabulary with accurate, concise definitions.
8. A technical brief that explains the concept beyond the student slide:
   - what the concept formally means;
   - how Python/the selected library behaves;
   - why the syntax or architecture is used;
   - what the teacher should and should not claim;
   - expected code output or visible application behavior;
   - important edge cases and limitations.
9. Deck guidance that tells the teacher how to use the relevant review, explanation, prediction, guided exercise, Bug Hunt, mini-project, workshop, and closing sections.
10. A timed teaching flow with teacher actions, student actions, transitions, questions to ask, and checkpoints.
11. Common misconceptions and likely errors with the exact diagnosis and correction.
12. Assessment evidence and observable success criteria.
13. Differentiation: minimum goal, support/scaffolding, and optional bonus.
14. Wrap-up, exit ticket, next-meeting connection, and any after-class preparation.

Do not use generic repeated text when a meeting requires a specific technical explanation. For example, a lesson plan must distinguish missing `self`, missing `super().__init__()`, class-versus-instance mistakes, duplicate GUI roots, and circular imports instead of labeling all of them merely as “syntax errors.”

### E. Technical Explanation Standard

For every important code pattern shown in the deck, the lesson plan must tell the teacher:

- what each new line or block is responsible for;
- what runs automatically and what must be called explicitly;
- the order in which objects, methods, callbacks, windows, modules, or data are created and used;
- the expected terminal output, GUI state, game behavior, file result, web result, or API/AI response;
- what students should predict before running;
- the most likely error message and its real cause;
- how to demonstrate the fix without replacing student thinking;
- which parts are required syllabus knowledge and which are optional extensions.

Technical accuracy overrides analogy. For example:

- `self` is the instance reference passed to an instance method, not a magic storage box;
- `__init__` initializes an already created instance and should not be described as literally creating the object;
- `super()` follows Python’s method resolution order and is not simply “the parent object”;
- inheritance should model an “is-a” relationship, while composition models a “has-a” relationship;
- two `Tk`/`CTk` root windows are an architectural mistake; use one root plus Frame or Toplevel as appropriate;
- importing a module executes its top-level code once per process and circular imports can expose partially initialized modules;
- double-underscore attributes use name mangling and are not truly inaccessible private data.

### F. Meetings 1–8 Lesson-Plan Guidance

The lesson plan must prepare the teacher to facilitate the student-deck cycle rather than merely list it:

- state the answers and reasoning for the minimum five active-review prompts;
- explain the formal concept, computer model, analogy boundary, minimal example, and expected result;
- provide facilitation notes for exactly three guided exercises per objective;
- identify when answers must remain hidden until students attempt the task;
- provide Bug Hunt diagnosis, expected error, and correction sequence;
- define the independent exercise acceptance criteria without turning it into a full solution;
- explain how the three guided mini-projects connect current and previous concepts;
- clarify the independent mini-project minimum goal, hints, likely blockers, and review method.

### G. Meetings 9–12 Lesson-Plan Guidance

For project workshops and showcase sessions, include teacher-facing operational detail:

- Meeting 9: approval criteria, feasible versus over-scoped examples, three-feature MVP rule, feature-to-syllabus mapping, class/data/game/app flow, risks, dependencies, milestones, and definition of done.
- Meeting 10: folder and environment verification, build checkpoint order, starter architecture boundaries, progress evidence, debugging triage, pitch coaching, and what qualifies as a working MVP/core mechanic.
- Meeting 11: required-feature completion, concrete positive/negative test cases, QA evidence, polishing order, README/user-guide expectations, screenshots/video backup, PPT structure, rehearsal protocol, and readiness status.
- Meeting 12: final file check, presenter flow, level-specific technical explanation, demo and backup sequence, visible criteria, timekeeping, audience behavior, Q&A coaching, honest handling of unknown answers, reflection, and celebration.

Project gallery examples must be translated into teacher guidance. Explain what is achievable, which learned concepts each feature uses, and which features are optional because they fall outside the syllabus.

### H. Layout, Print, and File Rules

- Use one standalone lesson-plan HTML file per requested level unless the user requests another structure.
- Use semantic HTML and local assets; the document must remain readable without internet access.
- Format print-oriented lesson plans as true A4 pages with `@page { size: A4; }`, predictable page breaks, sufficient margins, page numbers, and no clipped content.
- Use the Kalananti blue/yellow visual system with restrained decoration, clear hierarchy, readable tables, and strong contrast.
- Keep body text comfortable for teacher reading; avoid tiny fonts, oversized empty areas, dense walls of text, and decorative elements that compete with content.
- The ordinary HTML view should show the document directly. Do not add custom “Save as PDF,” print, page-jump, or developer toolbars unless the user explicitly requests them.
- Browser print remains available through the browser itself; custom print JavaScript is unnecessary by default.
- Every page should carry a clear header/footer and the correct local Kalananti logo when requested.
- Preserve the logo’s original colors; do not invert, recolor, stretch, blur, or crop it.
- Do not rely on external fonts, CDNs, or remote images for essential rendering.

### I. Lesson-Plan Quality Checks

Before completion:

- verify every syllabus objective and every deck section has corresponding teacher guidance;
- verify meeting timings add up to the stated duration;
- verify all preparation steps are actionable and no placeholder remains;
- verify code, output, and error explanations are accurate;
- verify project requirements trace only to the same level’s Meetings 1–8;
- verify each meeting states what students should know before class and what evidence they should produce by the end;
- verify the document contains no internal audit/provenance sections;
- verify all pages render at A4 size without vertical or horizontal clipping;
- verify all local logos/assets load and browser console has no unexplained errors;
- inspect representative pages visually, including the cover, overview, one concept meeting, one workshop meeting, and showcase.

## 5. Slide Count and Content Density

The normal target is a dense, informative, and student-friendly deck—not a padded deck.

- Meetings 1–8: target 45 slides per meeting. A range of 42–48 is acceptable only when objective count or topic complexity genuinely requires it.
- Meetings 9–11: target approximately 45 workshop slides per meeting. Use checkpoints, planning frameworks, examples, build milestones, debugging clinics, testing, pitch preparation, and reflection—not filler.
- Meeting 12: prioritize actual student presentation time. Use approximately 20–30 fixed instructional/showcase slides. It may approach 45 only when the extra slides have a real function such as presenter cards, timers, rubric reminders, transitions, peer feedback, or reflection.

Slide-density rules:

- One main teaching idea per slide.
- Split long explanations across slides; never use a wall of text to reach a slide target.
- Code must be readable from a classroom projector.
- Alternate explanation, visualization, prediction, interaction, coding, debugging, and reflection.
- A slide must earn its place by teaching, prompting thought, supporting practice, or guiding project work.

## 6. Global Navigation and Objective Jump Menu

Every level deck MUST include:

1. Twelve meeting tabs.
2. Previous/next slide controls and a visible slide counter/progress indicator.
3. A section/objective dropdown placed OUTSIDE the slide canvas/content, preferably in the upper-right toolbar.

The objective dropdown MUST:

- Stay visible while slides change and never be inserted into `slideContent` or the rendered slide body.
- List sections for the current meeting only.
- Include entries such as Review, Learning Objectives, each Objective, Guided Mini-Projects, Independent Mini-Project, and Closing.
- Use project-specific sections for Meetings 9–12.
- Jump to the first slide of the selected section.
- Automatically stay synchronized with the currently displayed slide.
- Be generated from slide metadata rather than a separately maintained manual list.
- Work with mouse, keyboard, and touch.
- Remain usable on laptop, projector, tablet, and mobile layouts without covering the slide.

Each slide data object should include stable navigation metadata, for example:

```js
{
  title: "...",
  sectionId: "objective-1",
  sectionLabel: "Objective 1 — Variables",
  objectiveId: "OBJ-1",
  content: "..."
}
```

## 7. Meetings 1–8 — Concept Learning Flow

Every concept-learning meeting MUST follow this sequence.

### A. Opening and Review

1. Meeting cover/title.
2. A minimum of five interactive review slides covering the previous meeting.
3. Meeting 1 reviews the previous level; Level 1 Meeting 1 reviews Trial Class or uses a diagnostic warm-up.
4. Review must use active recall rather than five passive summary slides. Rotate formats such as:
   - predict the output;
   - find the bug;
   - complete the code;
   - reorder code blocks;
   - concept quiz;
   - explain with an analogy;
   - quick VS Code challenge.

### B. Learning Objectives

- Convert the syllabus objective/activity breakdown into two or three measurable objectives when appropriate.
- Use observable outcomes. Example: “Students can create three variables with different data types and print them without a `NameError`,” not only “Students understand variables.”
- Do not add objectives outside the syllabus merely to fill slides.

### C. Scaffolded Cycle — Repeat for Each Objective

For each objective, include:

1. Objective section divider and success indicator.
2. Accurate technical/formal explanation using the original programming terminology.
3. A visual or step-by-step model of what the computer does.
4. An everyday analogy appropriate for junior-high-school students.
5. A minimal code example and its expected output/visual result.
6. A “predict before running” interaction.
7. Tips and tricks, programming do/don't, common mistakes, and a concept-specific debugging routine.
8. Exactly three guided exercises per objective—not three exercises per explanation slide. The teacher and students solve these together.
9. At least one Bug Hunt/debugging challenge.
10. One independent exercise with hints and an answer hidden by default in an accessible dropdown/reveal control. Reveal only after students have attempted it.

Guided exercise solutions should also be hidden by default so the prompt is discussed before the solution is shown.

### D. Integrated Practice

After all objectives are complete:

1. Provide three guided mini-projects integrating the meeting objectives. Show the problem first and hide each worked solution by default.
2. Provide one independent mini-project combining the current meeting and relevant previous meetings.
3. Do not provide the final answer/source code for the independent mini-project.
4. The independent mini-project may include requirements, starter code, example input/output, hints, acceptance criteria, and optional bonus goals.

### E. Closing

Include separate student-facing slides for:

- debugging recap;
- summary/key takeaways;
- exit ticket or reflection;
- preview of the next meeting where appropriate;
- Quote of the Day as its own final slide.

The Quote of the Day must be unique for every meeting, accurately attributed, age-appropriate, and never fabricated.

## 8. Interactive Activities for Online and Offline Classes

Every meeting must support both online and offline classroom delivery.

- Core navigation, answer reveals, quizzes, and section jumping must not require an internet connection after the deck and its local assets are loaded.
- Do not make a core activity depend only on an external CDN, remote image, API, or website.
- Provide an offline equivalent for online interactions where appropriate, such as hand signals, answer cards, pair discussion, paper prediction, whiteboard tracing, or running the same code in VS Code.
- Interaction must be meaningful: prediction, choice, manipulation, debugging, coding, discussion, or reflection—not decorative animation only.
- Answer/reveal controls must be hidden by default, keyboard accessible, and visibly indicate their open/closed state.
- Provide a clear fallback message when a runnable browser example is unavailable offline.

## 9. Meetings 9–11 — Final Project Workshop

Meetings 9–11 use everything learned in Meetings 1–8 to design, build, test, refine, and pitch one final project. Do not repeat the concept-session mini-project formula here.

Every workshop meeting should still include a short opening, active recall/project-status check, clear objectives, hands-on checkpoints, debugging support, reflection, and a unique Quote of the Day.

### Meeting 9 — Ideation and Project Planning

Students must leave with a feasible project proposal. Include:

- a flashback spanning the essential skills from Meetings 1–8;
- level-specific examples and inspiration;
- problem and target-user discovery;
- idea generation and selection;
- MVP versus optional bonus features;
- feature-to-syllabus mapping;
- input–process–output or application/game/data flow;
- pseudocode, flowchart, wireframe, class diagram, or level map as appropriate to the level;
- feasibility and dependency checks;
- milestones for Meetings 9–11;
- a copy-ready Google Docs project-planning framework.

The copy-ready framework should include: project name, problem, target user, proposed solution, three required MVP features, bonus features, concepts from Meetings 1–8, program flow, assets/data needed, possible errors/risks, milestones, and definition of done.

### Meeting 10 — Core Build and Pitch Draft

Students must leave with a working MVP/core mechanic. Include:

- project folder/setup verification;
- a build plan split into small milestones;
- starter architecture or pseudocode, without replacing the student's project with a full final answer;
- implementation checkpoints;
- level-specific debugging clinics;
- test-as-you-build guidance;
- progress evidence such as screenshots or a build journal;
- introduction to the elevator pitch;
- a first 45–60 second pitch draft;
- an initial presentation/PPT outline.

### Meeting 11 — Completion, Testing, and Presentation Preparation

Students must leave with a presentation-ready project. Include:

- completion of required features;
- test cases and a student-facing QA checklist;
- debugging and failure recovery;
- UI/output/gameplay/data/AI polishing appropriate to the level;
- screenshots and demo preparation;
- backup demo evidence in case the live application fails;
- a concise user guide or README outline;
- a 5–7 slide presentation framework;
- elevator-pitch refinement;
- rehearsal, peer feedback, and final readiness checklist.

Project planning, elevator-pitch examples, PPT structure, debugging advice, and demonstration style MUST be tailored to the level. Do not reuse generic final-project slides across all levels.

## 10. Meeting 12 — Showcase and Presentation

Meeting 12 is primarily student presentation time. Include only student-facing support needed to run a confident showcase:

- final technical and file check;
- presentation-day checklist;
- how to open with a hook;
- how to explain the problem, target user, solution, and key feature;
- how to explain code without reading every line;
- live-demo sequence and backup plan;
- time-management guidance;
- audience etiquette and useful peer-feedback prompts;
- handling questions and saying “I don't know yet” honestly;
- level-specific demo expectations;
- student-visible presentation criteria;
- reflection, celebration, closing, and a unique Quote of the Day.

Detailed teacher scoring forms, teaching procedures, and facilitator timing belong in a separate lesson-plan/rubric artifact unless explicitly requested.

## 11. Level-Specific Pitch and Demo Expectations

- Level 1 — Basic Python: explain input–process–output, condition/loop logic, and demonstrate the terminal program.
- Level 2 — Data Manipulation: show data before/after manipulation or explain the construction of a Turtle visual.
- Level 3 — GUI: present the user problem, screen flow, widgets, events, and live desktop-app interaction.
- Level 4 — OOP: explain the object/class model, important attributes/methods, and object interaction in the application.
- Level 5 — Platformer: explain the core mechanic, controls, collision/physics, scoring, challenge, game balance, and playtest.
- Level 6 — Web + AI: explain the user problem, web flow, AI/API role, prompt or data flow, limitations, privacy, and responsible use.

## 12. Final Project Alignment

- Treat `level/source-code/` as a north-star gallery of possible personal projects, not as code students should copy blindly.
- Inspect all available examples for the requested level before designing Meetings 9–12.
- Build a traceability map from every required project feature to a concept learned in Meetings 1–8.
- Keep the MVP achievable within Meetings 9–11.
- Separate required MVP features from optional “Silver/Gold” bonus scope for faster students.
- Do not require an unavailable example project for Levels 1 or 2; use the syllabus project directions until aligned examples are added.
- Never change the syllabus library to match an old example. Adapt or replace the example later.

## 13. Runnable Code and VS Code

VS Code is the primary student development environment. Browser runners are practice aids, not replacements for creating and running `.py` files.

Use runnable code only when the technology genuinely supports it:

- Console Python: Pyodide/PyScript or another verified browser runner.
- Programs using `input()`: use a runner with a working simulated terminal input, or run in VS Code.
- Turtle: use a verified browser-compatible Turtle implementation or run in VS Code.
- File handling: use a clearly explained browser sandbox or run in VS Code.
- Tkinter/CustomTkinter: run in local VS Code; show code plus the expected visual result in the deck.
- Arcade/Pygame: run in local VS Code; show code plus the expected game visual/behavior in the deck.
- Streamlit: run through the VS Code terminal and open the local browser URL.
- External AI/API calls: run locally with protected environment variables and an offline/mock fallback where possible.

Never show a Run button that does nothing. A runnable block must have an editor or starter code, Run, Reset, visible output, friendly error state, and any required input mechanism. Test its code and expected output before completion.

Recommend VS Code extensions only when relevant, such as:

- Python by Microsoft;
- Pylance;
- Python Debugger;
- Error Lens as an optional visual aid;
- Black Formatter or Ruff for later levels.

Do not recommend Live Server as a universal Python requirement.

## 14. Pedagogy, Language, and Accessibility

- Student audience: junior-high-school learners unless the user specifies otherwise.
- Primary explanation language: clear Bahasa Indonesia.
- Preserve and define the original English programming terminology.
- Explain accurately first, then elaborate with a familiar analogy. Never let the analogy replace or contradict the technical definition.
- Use meaningful variable/function names and consistent Python formatting.
- Provide minimum goal, staged hints, and optional bonus challenges so mixed-ability classes can participate.
- Encourage students to explain their code; copying without understanding is not mastery.
- Never shame mistakes. Treat errors as evidence that helps debugging.
- Ensure strong contrast, readable font sizes, keyboard access, visible focus states, and instructions that do not depend on color alone.

Use a consistent debugging routine, for example:

1. Read the error message.
2. Locate the indicated line.
3. Check spelling, punctuation, type, indentation, and program state.
4. Fix one cause at a time.
5. Run again and compare actual versus expected behavior.

## 15. Security and Responsible AI

- Never expose API keys, passwords, tokens, student personal data, or secrets in HTML, JavaScript, screenshots, or committed source code.
- Use environment variables such as `.env` for local API keys and ensure secret files are ignored by version control.
- Clearly distinguish a rule-based simulation from a real LLM/AI API.
- Do not render untrusted user input with unsafe HTML helpers.
- Teach students that AI output may be incorrect and must be checked.
- Include age-appropriate privacy, copyright, bias, safe prompting, and responsible-use reminders in Level 6.
- Technical explanations must be accurate. For example, Python double-underscore attributes use name mangling; they are not truly inaccessible private data.

## 16. Student Deck Definition of Done

Do not claim a deck is complete until all applicable checks pass:

- [ ] `AGENTS.md`, the full syllabus, the relevant previous material, and relevant source examples were read first.
- [ ] The deck has exactly 12 meeting tabs.
- [ ] Slide count is appropriate for the meeting type and no filler was used.
- [ ] The external objective/section dropdown works and stays synchronized.
- [ ] Previous, next, keyboard, touch, counter, and progress navigation work.
- [ ] Meetings 1–8 include at least five active-review slides.
- [ ] Every syllabus objective is covered and traceable.
- [ ] Every objective has technical explanation, computer model/visual, everyday analogy, code/result, do/don't, debugging, exactly three guided exercises, and one independent exercise.
- [ ] Guided and independent answers are hidden by default; the independent mini-project has no final answer.
- [ ] Online and offline interaction paths are both usable.
- [ ] Meetings 9–11 produce the required planning, build, testing, pitch, and presentation deliverables.
- [ ] Meeting 12 prioritizes presentation and includes a level-specific showcase flow.
- [ ] Final-project requirements map to Meetings 1–8 and use the syllabus technology.
- [ ] All code examples were syntax/output checked and runnable controls were functionally tested.
- [ ] Browser console shows no unexplained errors.
- [ ] No broken assets, horizontal overflow, unreadable code, or controls covering the slide.
- [ ] The deck works on common laptop/projector sizes and remains usable on smaller screens.
- [ ] Quotes are unique, accurately attributed, and placed on their own final slide.
- [ ] No secrets, unsafe user-input rendering, or false AI claims are present.
- [ ] Teacher-only lesson-plan content was not mixed into the student deck.

## 17. Lesson Plan Definition of Done

Do not claim a lesson plan is complete until all applicable checks pass:

- [ ] The user explicitly requested a teacher-facing lesson plan or equivalent artifact.
- [ ] The full syllabus, requested deck, relevant previous material, and all relevant source examples were read first.
- [ ] Internal source audits, repository paths, validation tables, and developer notes are absent from the teacher document.
- [ ] The cover uses the correct Kalananti logo without filters or distortion.
- [ ] The program overview explains the learning journey, prior knowledge, final outcome, and teacher/student preparation.
- [ ] Every meeting states duration, objectives, prior knowledge, student preparation, teacher preparation, materials, and expected evidence.
- [ ] Every meeting includes a detailed technical brief, vocabulary, deck guidance, timed flow, misconceptions, likely errors, assessment, differentiation, and wrap-up.
- [ ] Important deck code patterns include expected results, execution order, likely error messages, and accurate correction guidance.
- [ ] Meetings 1–8 prepare the teacher for review, explanation, prediction, three guided exercises per objective, Bug Hunt, independent work, and integrated practice.
- [ ] Meetings 9–11 contain concrete project approval, build, testing, pitch, documentation, and readiness guidance.
- [ ] Meeting 12 contains a level-specific presentation flow, demo/backup plan, visible criteria, Q&A support, peer feedback, and reflection.
- [ ] Required project features are traceable to Meetings 1–8; out-of-syllabus gallery features are clearly optional.
- [ ] Online and offline preparation paths are both included.
- [ ] Timings add up consistently and are realistic for the stated meeting duration.
- [ ] The HTML uses local essential assets and contains no custom print/navigation controls unless requested.
- [ ] All A4 pages render without clipped text, broken assets, unreadable tables, or excessive empty space.
- [ ] Browser console has no unexplained errors and representative pages were visually inspected.

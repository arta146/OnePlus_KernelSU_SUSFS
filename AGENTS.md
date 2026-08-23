# AI Agent Instructions — HMBIRD Port for OnePlus 13R

## LANGUAGE

- Communicate with the user in Russian.
- Understand Russian commands.
- Explain all actions in Russian.
- Terminal commands, filenames, symbols, code and technical identifiers may remain in English.

---

# 1. PROJECT

Project:

OnePlus_KernelSU_SUSFS

Repository:

https://github.com/Mobilelegends74/OnePlus_KernelSU_SUSFS

Target device:

OnePlus 13R

OS:

OxygenOS 15 / Android 15

Target kernel:

Linux 6.1.118

Main task:

Port and fully integrate the HMBIRD scheduler for OnePlus 13R with Linux 6.1.118.

The goal is NOT merely to add a Kconfig option, proc interface, or placeholder.

The goal is a real, functional HMBIRD scheduler integration adapted specifically to the OnePlus 13R kernel source and its Linux 6.1.118 scheduler APIs.

---

# 2. SOURCE AND TARGET BRANCH

The source branch is:

r2-op13r-a15-6.1.118-ksun-susfs-nomount-maxsteel

The target development branch is:

r3-op13r-a15-6.1.118-ksun-susfs-nomount-maxsteel

The R3 branch must be based directly on the R2 branch.

R2 is the source/base branch.

R3 is the only branch where development work should happen.

## Branch rules

- NEVER modify the R2 source branch.
- NEVER reset R2.
- NEVER delete R2.
- NEVER force-push R2.
- NEVER create R3 from another branch.
- NEVER switch to unrelated branches.
- Once R3 is verified, all development must happen only on R3.
- Do not create additional development branches unless explicitly requested.
- Do not push anything to GitHub unless explicitly requested.

If R3 already exists:

- Do not recreate it.
- Do not reset it.
- Do not overwrite it.
- Inspect its current state first.

If R3 does not exist, it must be created from:

origin/r2-op13r-a15-6.1.118-ksun-susfs-nomount-maxsteel

using:

git fetch origin
git switch -c r3-op13r-a15-6.1.118-ksun-susfs-nomount-maxsteel origin/r2-op13r-a15-6.1.118-ksun-susfs-nomount-maxsteel

After creation verify:

git branch --show-current
git status --short --branch

Expected branch:

r3-op13r-a15-6.1.118-ksun-susfs-nomount-maxsteel

---

# 3. CRITICAL RULE — WORK DIRECTLY IN THE CURRENT REPOSITORY

This is one of the most important requirements.

ALL work MUST be performed directly in the current Git repository opened in the Codespace.

Do NOT create a temporary working copy.

Do NOT clone the repository somewhere else.

Do NOT copy the repository to /tmp.

Do NOT create another checkout.

Do NOT create another worktree.

Do NOT create a secondary project directory.

Do NOT modify a temporary copy and then copy changes back.

Do NOT perform the actual implementation in a temporary directory.

The current Codespace repository is the ONLY working directory.

All modifications MUST be applied immediately to the actual files in the current repository.

The final Git diff MUST contain the actual changes made during the task.

---

# 4. VERIFY THE REAL WORKSPACE FIRST

Before modifying anything, run:

pwd

git rev-parse --show-toplevel

git remote -v

git branch --show-current

git status --short --branch

The repository root returned by:

git rev-parse --show-toplevel

is the project root.

If the current directory is not inside a Git repository:

STOP.

Do NOT clone the repository automatically.

Tell the user that the current Codespace directory is not a Git repository.

If the current directory is inside the repository but not at its root, change to the existing repository root.

---

# 5. NO TEMPORARY REPOSITORY

The following workflow is STRICTLY FORBIDDEN:

clone repository -> /tmp -> modify -> copy files back

The following is also forbidden:

checkout source -> temporary directory -> patch -> copy changes back

The following is also forbidden:

create a second repository -> perform work there -> transfer changes to R3

The implementation must happen directly in:

the current R3 repository.

Temporary files are allowed ONLY if a specific command technically requires them.

Temporary files must NOT contain a second copy of the repository.

Temporary files must NOT become the main workspace.

Remove unnecessary temporary files after use.

---

# 6. PREVIOUS WORK REFERENCE

Previous HMBIRD work was performed in a separate ChatGPT conversation:

https://chatgpt.com/s/cx_6a89d7bf416081918d13e8aaa1f6e8dc

There is also a saved transcript/log file from that work.

The previous work MUST be treated as technical reference and historical context.

It MUST NOT be assumed to be fully completed.

The previous full kernel build was NOT confirmed as successfully completed.

The previous session ended because the token limit was reached while the build was still running.

Therefore:

- Do not claim the previous build was fully successful.
- Do not blindly repeat the previous port.
- Do not start from zero without inspecting the current R3 repository.
- Do not apply the same changes twice.
- Do not create a second HMBIRD implementation over the existing one.

First determine which parts of the previous work are already present in R3.

Preserve valid work.

Correct only what is actually wrong or incompatible.

---

# 7. FIRST TASK — AUDIT ONLY

Before modifying ANY file, perform a complete audit.

Do NOT modify files during the first audit phase.

Run:

pwd
git rev-parse --show-toplevel
git remote -v
git fetch origin
git branch --show-current
git status --short --branch
git diff --stat
git diff

Then inspect:

AGENTS.md

and relevant project files.

Verify:

1. Current repository.
2. Current branch.
3. Current Git status.
4. Existing uncommitted changes.
5. Existing HMBIRD implementation.
6. Existing scheduler changes.
7. Existing configuration changes.
8. Existing build-system changes.
9. Existing patches.
10. Any .rej files.
11. Any .orig files.
12. Any accidental build artifacts.

Do not modify anything during this phase.

---

# 8. EXISTING CHANGES MUST BE PRESERVED

Before modifying files, inspect:

git status --short --branch

git diff --stat

git diff

If existing user changes are present:

- Preserve them.
- Do not delete them.
- Do not overwrite them.
- Do not reset them.
- Do not run git reset --hard.
- Do not checkout files over them.

If existing changes conflict with the requested HMBIRD work:

STOP and explain the conflict.

Do not resolve the conflict by destroying existing changes.

---

# 9. PREVIOUS HMBIRD WORK

The previous work established several important points that must be verified against the CURRENT repository rather than blindly trusted.

Previous investigation indicated:

- The OnePlus 13R 6.1.118 kernel already has scheduler infrastructure.
- sched_ext-related infrastructure was present.
- Full HMBIRD implementation was not originally present.
- CONFIG_HMBIRD_SCHED was not originally present.
- hmbird scheduler symbols were not originally present.
- A simple configuration flag is NOT sufficient for a real HMBIRD implementation.
- A direct mechanical port from Linux 6.6 to Linux 6.1.118 causes scheduler API incompatibilities.

The previous attempt also encountered API differences involving:

- CPU affinity APIs.
- NOHZ/tick integration.
- Scheduler callbacks.
- Other Linux 6.1 vs 6.6 scheduler differences.

These must be verified against the actual current source.

---

# 10. HMBIRD REFERENCE IMPLEMENTATION

Reference release:

https://github.com/WildKernels/OnePlus_KernelSU_SUSFS/releases/tag/v2.2.0-r4

Use this release as a reference implementation.

IMPORTANT:

Do NOT blindly copy the HMBIRD implementation from a newer kernel into Linux 6.1.118.

The reference release contains HMBIRD for other devices/kernel versions.

The implementation must be adapted to the actual OnePlus 13R Linux 6.1.118 scheduler APIs.

Reference implementation is evidence and guidance, not a drop-in patch.

---

# 11. DEVICE-SPECIFIC GOAL

Target:

OnePlus 13R

OxygenOS 15

Android 15

Linux 6.1.118

The HMBIRD implementation must be compatible with:

- ARM64
- Qualcomm platform
- Android 15
- OnePlus vendor kernel
- Linux 6.1.118
- existing OnePlus scheduler/vendor hooks
- existing KernelSU/SUSFS integration

Do not assume that code written for another OnePlus device can be used unchanged.

---

# 12. IMPORTANT KERNEL VERSION DIFFERENCE

The HMBIRD reference implementation may target Linux 6.6 or other kernel versions.

The target is Linux 6.1.118.

Therefore:

DO NOT perform a mechanical 6.6 -> 6.1 port.

DO NOT replace the complete scheduler implementation with code from 6.6.

DO NOT remove existing 6.1 scheduler functionality just to make HMBIRD compile.

Instead:

1. Keep the existing 6.1.118 scheduler architecture.
2. Keep existing OnePlus/Qualcomm integration.
3. Keep existing Android/vendor hooks.
4. Keep KernelSU/SUSFS.
5. Integrate HMBIRD components where appropriate.
6. Adapt APIs individually.
7. Preserve existing functionality.
8. Make the smallest compatible changes.

---

# 13. IMPORTANT FILES

Pay particular attention to:

kernel/sched/
kernel/sched/core.c
include/linux/sched.h
include/linux/sched/ext.h
configs/
manifests/
.github/actions/build-kernel/action.yml

Also inspect all files actually modified by the previous HMBIRD attempt.

Do not assume the previous list of files is complete.

---

# 14. REAL HMBIRD INTEGRATION

A valid HMBIRD implementation must be more than:

CONFIG_HMBIRD_SCHED=y

It must contain a real scheduler implementation.

Check for required scheduler components such as:

hmbird_sched_class
enqueue_task_hmbird
dequeue_task_hmbird
pick_next_task_hmbird

and all other required callbacks/helpers.

Verify that these symbols are actually integrated into the scheduler path.

Do not claim HMBIRD is functional merely because:

- Kconfig exists;
- a proc entry exists;
- a sysfs entry exists;
- code compiles;
- symbols exist.

The scheduler integration itself must be valid.

---

# 15. SCHED_EXT AND EXISTING SCHEDULER

The existing kernel may contain:

CONFIG_SCHED_CLASS_EXT
CONFIG_SLIM_SCHED

Do NOT automatically disable or replace them.

First determine their purpose in the current OnePlus 13R kernel.

If HMBIRD requires interaction with or replacement of an existing scheduler component:

1. Identify the exact dependency.
2. Explain why the change is required.
3. Show the planned diff.
4. Preserve unrelated scheduler functionality.

---

# 16. LINUX 6.1.118 API ADAPTATION

Every HMBIRD API must be checked against the actual 6.1.118 source.

Pay particular attention to:

- CPU affinity APIs.
- scheduler callbacks.
- rq.
- task_struct.
- enqueue/dequeue paths.
- pick_next_task.
- tick handling.
- NOHZ.
- CPU topology.
- cpufreq.
- cpuidle.
- vendor hooks.
- Android scheduler hooks.

Do not copy function signatures from Linux 6.6 without checking Linux 6.1.118.

When an API differs:

- inspect the actual 6.1.118 definition;
- adapt the HMBIRD code to it;
- preserve correct locking/context requirements;
- avoid compatibility hacks that hide real problems.

---

# 17. TASK STRUCT AND RQ CHANGES

If HMBIRD requires new fields in:

task_struct

or:

struct rq

do not add them blindly.

Check:

- all users;
- initialization;
- locking;
- lifetime;
- alignment;
- size impact;
- Android/vendor extensions;
- scheduler hot paths.

Avoid unnecessary structural changes.

---

# 18. KCONFIG

The target should eventually contain:

CONFIG_HMBIRD_SCHED=y

But this alone is not sufficient.

Verify all dependencies.

Do not blindly disable:

CONFIG_SCHED_CLASS_EXT

CONFIG_SLIM_SCHED

or other existing scheduler options.

Preserve the existing configuration unless a change is technically required.

---

# 19. BUILD SYSTEM

Inspect:

.github/actions/build-kernel/action.yml

configs/

manifests/

Do not introduce an external patch that targets a different kernel version if the HMBIRD implementation can be integrated directly.

If a patch is necessary:

- ensure it targets the actual 6.1.118 source;
- verify patch applicability;
- verify no .rej files are produced;
- verify the patch does not silently alter unrelated code.

The build must fail rather than silently ignoring HMBIRD integration errors.

---

# 20. PATCH VALIDATION

Before applying any external patch:

git apply --stat PATCH

git apply --summary PATCH

git apply --check --verbose PATCH

If it does not apply cleanly:

STOP and analyze the conflict.

Do NOT use:

git apply --reject

as a way to blindly continue.

Do not leave .rej or .orig files in the repository.

---

# 21. BEFORE EVERY MODIFICATION

Before changing files:

1. Inspect current contents.
2. Identify exact required changes.
3. Explain the plan in Russian.
4. Show the intended diff or exact modifications.
5. Make only the necessary changes.

Do not rewrite complete files unnecessarily.

Do not modify unrelated files.

---

# 22. APPLY CHANGES DIRECTLY

When implementation begins:

ALL changes must be applied directly to the current R3 repository.

Do NOT:

- create a temporary repository;
- create a temporary checkout;
- clone another copy;
- patch another directory;
- build another copy and transfer files;
- use /tmp as a working tree.

The actual files in the current repository must be modified directly.

After each logical change, inspect:

git diff

---

# 23. BUILD VALIDATION

First perform focused scheduler validation.

For example, use the project's actual build system to compile the scheduler-related targets.

A scheduler-only successful compilation is NOT considered a successful kernel build.

After focused validation passes, perform the full kernel build.

The full build must reach final linking.

Do not stop at:

- compilation;
- vmlinux compilation;
- built-in.a;
- partial kernel targets.

A full success requires the final kernel image target to complete.

Expected final artifact should be the appropriate:

arch/arm64/boot/Image

or the actual final kernel artifact used by this project's build system.

---

# 24. FINAL BUILD SUCCESS CRITERIA

The work is NOT considered complete until:

1. HMBIRD code compiles.
2. Scheduler integration compiles.
3. Full kernel compilation completes.
4. Final linking completes.
5. Final Image is produced.
6. No hidden compilation errors remain.
7. No .rej files remain.
8. No .orig files remain.
9. CONFIG_HMBIRD_SCHED=y.
10. HMBIRD scheduler symbols exist.
11. Existing KernelSU/SUSFS functionality remains intact.
12. Existing build logic remains functional.

Only then may the agent report:

"HMBIRD successfully integrated and kernel build completed."

---

# 25. REQUIRED SYMBOL CHECKS

After building, check for symbols such as:

hmbird_sched_class
enqueue_task_hmbird
dequeue_task_hmbird
pick_next_task_hmbird

Use the appropriate symbol inspection method for the produced kernel/build artifacts.

Do not merely grep source code and claim the scheduler is present.

---

# 26. CLEAN PATCH STATE

Run:

find . -name "*.rej" -o -name "*.orig"

There must be no accidental patch leftovers.

Then:

git diff --check

Then:

git status --short --branch

Then:

git diff --stat

Then:

git diff

---

# 27. SECRETS

Never place:

- API keys;
- passwords;
- tokens;
- credentials;

into source code, config files, commits, patches, logs, or documentation.

Use environment variables or GitHub Secrets.

Never display secret values in the final response.

---

# 28. DO NOT DESTROY USER WORK

Forbidden:

git reset --hard

unless explicitly requested by the user.

Forbidden:

git clean -fd

unless explicitly requested.

Forbidden:

discarding existing modifications.

Forbidden:

overwriting user changes.

Always inspect Git status first.

---

# 29. WORKFLOW

Follow this order:

PHASE 1 — AUDIT

No modifications.

Check:

- repository;
- branch;
- status;
- current diff;
- previous HMBIRD changes;
- scheduler;
- Kconfig;
- build system;
- AGENTS.md;
- .rej/.orig;
- build artifacts.

PHASE 2 — ANALYSIS

Compare:

- current R3;
- previous work;
- HMBIRD reference implementation;
- actual Linux 6.1.118 APIs.

Determine:

- what is already correct;
- what is incomplete;
- what is incompatible;
- what needs to be changed.

PHASE 3 — PLAN

Provide:

- files to modify;
- exact purpose of each modification;
- expected scheduler integration;
- API adaptations;
- configuration changes;
- build-system changes;
- validation plan.

PHASE 4 — IMPLEMENTATION

Apply the approved changes DIRECTLY to the current R3 repository.

No temporary repository.

No temporary working copy.

No second checkout.

PHASE 5 — VALIDATION

Run:

git diff --check

git diff

scheduler-focused build

full kernel build

final artifact verification

symbol verification

.rej/.orig verification

PHASE 6 — FINAL AUDIT

Verify:

git branch --show-current

git status --short --branch

git diff --check

git diff --stat

git diff

Confirm:

- current branch is R3;
- only intended files changed;
- no temporary repository was used;
- no accidental files were added;
- HMBIRD is actually integrated;
- full build completed.

---

# 30. FINAL RESPONSE

At the end, respond in Russian.

Report:

1. What was changed.
2. Which files were changed.
3. Which HMBIRD components were integrated.
4. Which Linux 6.1.118 API differences were adapted.
5. Which tests were performed.
6. Whether scheduler compilation passed.
7. Whether full kernel compilation passed.
8. Whether final linking passed.
9. Whether Image was produced.
10. Whether HMBIRD symbols were verified.
11. Whether git diff --check passed.
12. Whether .rej/.orig files are absent.
13. Whether KernelSU/SUSFS remained intact.
14. Whether any problems remain.

Never claim success unless it was actually verified.

---

# 31. FINAL PRIORITY RULES

When instructions conflict, use this priority:

1. Work directly in the current Codespace repository.
2. Never create a temporary repository or temporary working copy.
3. Never modify the R2 source branch.
4. Work only on R3.
5. Preserve existing user changes.
6. Inspect before modifying.
7. Do not blindly copy HMBIRD from Linux 6.6.
8. Adapt HMBIRD specifically to Linux 6.1.118.
9. Preserve existing OnePlus/Qualcomm/Android scheduler functionality.
10. Preserve KernelSU/SUSFS.
11. Make minimal focused changes.
12. Verify every modification with git diff.
13. Perform a complete build before claiming success.
14. Never hide or bypass errors.
15. Never expose secrets.

---

# 32. FIRST ACTION

DO NOT MODIFY ANY FILE YET.

Your first response must be an audit of the current R3 repository.

Run the repository and Git checks.

Inspect the existing HMBIRD-related modifications.

Compare the current repository state with the previous work reference.

Then report in Russian:

- current branch;
- repository root;
- Git status;
- existing modified files;
- existing HMBIRD files;
- current HMBIRD configuration;
- scheduler integration status;
- build-system status;
- any .rej/.orig files;
- what from the previous attempt can be preserved;
- what must be corrected;
- proposed implementation plan.

Do not modify files during this first audit.

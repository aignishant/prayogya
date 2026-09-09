# Glossary — Prayoga

Append-only. One row per term, defined **once**, with the part that introduced it.

This file exists because 297 sittings is long enough that day 3 is forgotten by day 200. Its real
job is not to be read front to back; it is to be **checked before defining anything**, so a term
is never defined twice, slightly differently, in two places. Two nearly-identical definitions are
worse than one bad definition, because the reader cannot tell which is current.

Before you define a term in a day document, search this file. If it is here, link the part that
introduced it instead of redefining it.

| Term | Plain-language definition | Introduced in | Also called |
| ---- | ------------------------- | ------------- | ----------- |
| Authoring repository | The repository holding the plan, the ledgers and `./p`. It writes and checks the forty projects, and none of them depend on it. | day 0 part 2.1 | this repository |
| Project repository | One of the forty folders under `projects/`. Complete alone: its own pins, its own boundary, its own `./run`. | day 0 part 2.1 | a project |
| Driver | The one script a repository is operated through, so a command is found by reading one file rather than by remembering. `./p` here; `./run` inside every project. | day 0 part 3.1 | the runner |
| Depth contract | The plan section 5 rules on what a part document must contain, and the half of them `python p.py depth` can check by machine. | day 0 part 3.3 | the contract |
| Generated document | A file under `docs/` rebuilt from the days by `python p.py index`. Editing one only means the next run silently overwrites you. | day 0 part 3.4 | an index |
| Marker block | An HTML comment pair in the plan fencing a table `./p` parses. A heading can be reworded by accident; a marker cannot. | day 0 part 2.4 | the markers |
| Interpreter | The program that runs your code — one `python` executable at a real path, of one exact version. | day 0 part 1.1 | the interpreter |
| Environment | An interpreter together with a particular set of installed packages. Two environments on one machine can hold the same package at different versions and never see each other. | day 0 part 1.1 | — |
| Pin | A written-down exact version, recorded in a file so that a machine and not a memory decides what gets used. | day 0 part 1.1 | the pin |
| Search order | The list of places a machine walks to turn a name like `python` into one program on disk. First match wins, and nothing announces that there was a choice. | day 1 part 1.1 | discovery order |
| Virtual environment | A directory holding a link back to a real interpreter and its own installed packages, marked as one by a `pyvenv.cfg` beside the executable. Not a shell mode and not a variable. | day 1 part 1.2 | venv, the environment |
| Lockfile | The tool-written record of what a resolution actually produced — exact versions and content hashes — as against `pyproject.toml`, which records what was asked for. | day 1 part 2.1 | the lock, `uv.lock` |
| Tracked | A path git has been told to hold, from a `git add` onward. Ignore rules do not reach it: they speak only about paths git has never been told to hold. | day 2 part 1.1 | under version control |
| Staging area | The list of paths git is holding for the next commit — what `git add` writes into and `git rm --cached` removes from. A path in it is tracked, whatever any ignore rule says. | day 2 part 2.2 | git's index, the cache |
| Ignore source | One of the six places git reads exclude patterns from for a single path. Four are files in the repository; two are per-machine and invisible to review. | day 2 part 2.1 | exclude source |
| Negated pattern | An ignore line beginning `!`, which takes a path back out of the ignore list. It only works below the pattern it is excepting, because within one file the last match decides. | day 2 part 1.2 | a negation, an exception |
| Process environment | The set of name-to-string pairs the operating system handed a program when it started, which Python exposes as `os.environ`. It is built by whatever launched the program and has never heard of any file. | day 3 part 1.1 | the environment block, env vars |
| Floor | A dependency or interpreter requirement written as `>=`, which states what is too old and leaves the choice to whichever machine resolves it. Correct for a library, never sufficient for an application. | day 3 part 2.1 | a lower bound, a range |
| Exit status | The single number a process hands back when it ends, and the only channel through which a check reports its verdict to another program. Zero means success; everything printed to the screen is for humans. | day 3 part 2.2 | exit code, return code, `$?` |
| Model alias | A model name that stands in for whichever model currently holds a role rather than for a model — `-latest`, documented as hot-swapped on every release. A floor wearing a version's clothes. | day 4 part 1.1 | a moving name, `-latest` |
| Stateless | Of a server: it keeps nothing between one request and the next. There is no session to attach to and no identifier to quote back, so every request must carry everything its answer depends on. | day 4 part 1.3 | request/response, no server-side state |
| Turn | One piece of a conversation together with who produced it — a `role` of `user` or `model`, and the parts that make it up. Your question is a turn; the reply is a turn. | day 4 part 1.3 | a message, a `Content` |
| Candidate | One complete alternative answer in a provider's reply. The response carries a list of them, and this project ever asks for one; the words are inside its `content.parts`, not at the top level. | day 4 part 1.3 | a completion, a choice |
| Conversation | The ordered list of turns, and in a stateless system the only copy of it. Here it is `Conversation.contents`, an ordinary Python list in your own process, resent in full on every request. | day 4 part 2.1 | the thread, the transcript, history |
| System instruction | Standing orders sent beside the conversation rather than inside it — what the agent is for and what it may answer from. Not a turn, because nobody said it in the exchange, and resent on every request because the provider remembers nothing. | day 4 part 2.1 | the system prompt |
| Function declaration | The JSON object a model is given for one of your functions: a name, a prose description, and a JSON Schema for the arguments. It is the entire interface — the model never sees the code — and nothing checks that it describes the function correctly. | day 5 part 1.1 | tool declaration, the schema |
| JSON Schema | A standard vocabulary for describing the shape of a JSON value: its type, its named properties, and which of them are required. Used here to tell a model what an argument bag must look like, and it says nothing about defaults. | day 5 part 1.1 | the parameters schema |
| Tool call | A part of a model's reply that names a tool and carries an object of arguments, in place of the text it would otherwise have written. It is a request made of your program: the model cannot run anything itself. | day 5 part 2.1 | function call, `functionCall` |
| Tool-result turn | The message you append after running a tool, carrying one `functionResponse` part per call with the tool's return value verbatim. It is what makes one question cost at least two provider calls. | day 5 part 2.1 | the function response, the result turn |
| Agent (ADK) | A configuration object describing one agent — its name, its model, its description, its instruction and its tools. It is filled in, never subclassed, and it does no work on its own. `Agent` and `LlmAgent` are the same class. | day 6 part 1.1 | LlmAgent, the brief |
| Runner | The object that executes one turn for an agent: it holds the agent and the session service, and it produces the turn's events as they happen. The agent is the configuration; the runner is what runs it. | day 6 part 2.1 | the runner |
| Session | One stored conversation, identified by an app name, a user and a session id, held by a session service rather than by your code. It is where the list you resent by hand on day 4 now lives. | day 6 part 2.1 | the stored conversation, an ADK session |
| FunctionTool | ADK's wrapper around a plain Python function, which derives the model-facing declaration from the function object itself — name from `__name__`, parameter schema from the signature, description from the docstring. Assigning a function to an agent's `tools` list creates one automatically. | day 7 part 1.1 | the wrapper |
| Derived declaration | A tool declaration the framework builds by reading a function, as against one written by hand beside it. It cannot drift from the function, and it can only carry what the function already contains — which is why a per-parameter description has nowhere to live in one. | day 7 part 1.2 | the derived schema |

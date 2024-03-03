Thoth (To Do)
=======================

`thoth` is a todo cli app based on todo.txt format.

## Run project (dev) (linux)
```
source .venv/bin/activate
python3 -m pip install -e .
```

## Thoth commands
* `thoth init [path]` - Init todo -> must be done for first run. Defautlt path: current folder
* `thoth a [todo]` - Add a todo
* `thoth rm [id]` - Remove todo by id
* `thoth ls [-s] [sort_arg]` - List all todos and sort them by arg (default: priority)
* `thoth s [partial text]` - Search a specific to do by text

## Versions
### v1.0.0
- [x] Init command
- [ ] Add command
- [ ] List command
- [x] Todo parser
- [ ] Option: automatically add creation date

## To Do (Idea for future functionnality)
- [ ] Podoromo timer + distraction free terminal
- [ ] Terminal color for priority, projet tags, context tags
- [ ] Terminal theme customisation 
- [ ] Modify command
- [ ] Revert command (undo last action)

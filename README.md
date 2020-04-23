## Nuzlocke-SSG
A Static site generator for nuzlocke challenges

## TODO:
#### [Important]
- Make templates nicer (in progress)

#### [Not Important]
- Might add support for M/F sprites (probably not, this might require separating folders)

#### [Recently Finished]
- Copy sprite assets to build folder
    -Ideas: revamp sprite_dl. Instead of download to content folder download directly to build
    folder. Or giv the option to target of specific folder in the configs (nah this was dumb
    hardcode everything)
- img url should be included into PokemonData
- Better support for content generation (mainly posts) might need beautifulsoup
- Create a function that deletes Posts before build (might not need this)
- Fix templates when it hits 490 pixels width
- Fix titles in posts.html

#### [Possible variable name changes]
- change generate to "build" in functions
- Change index.html to just index.html [cant search and replace]
- change pokemon_list.html -> pokemon_list.html [cant search and replace]

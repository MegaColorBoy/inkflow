title: Prevent VIM from creating swapfiles
date: July 3rd, 2021
slug: prevent-vim-from-creating-swapfiles
category: VIM
status: active

I like VIM and use it regularly to write and edit code on a daily basis but I always find the creation of `.swp` files really annoying.

If you find them annoying too, you disable them temporarily in the editor, like this:

```vim
:set noswapfile
```

Or if you want to disable it permanently, just add this line in your `.vimrc` file:
```vim
set noswapfile
```

Don't get me wrong, I'm not saying that you should dislike `.swp` files because if the editor crashes or your computer/server crashes in midway, those files can save your progress.

Hope you found this tip useful!
title: Keep a programming journal using VIM and Bash
date: April 26th, 2019
slug: keep-a-programming-journal-using-vim-and-bash
category: Productivity
summary: Become a better programmer by writing your own programming journal using VIM and Bash.

Back in the days of Polymath scientists, physicists and engineers like [Leonardo Da Vinci](https://en.wikipedia.org/wiki/Leonardo_Da_Vinci) and [Albert Einstein](https://en.wikipedia.org/wiki/Albert_Einstein), they usually maintained a sort of journal to record their thoughts, ideas and experiments.

It's been 20 days since I have started maintaining journals, one is for personal stuff and the other is for programming, engineering and math related stuff, I mean, we all need to have some new hobbies to keep ourselves productive, right?

Maintaining a journal helped me create a flow to write down my experiences ofthe day. It also helps me clear my mind and be more emotionally stable (I get moody, sometimes) and record my thoughts and ideas too.

There are so many ways to write a journal like you could sign up on some online platform, install Evernote on your desktop or mobile or traditional pen and paper (which is the best way, honestly).

## Requirements

I thought of keeping it in my laptop and I wanted it to have the following features:

1. No use of internet required
2. Must be super fast, simple and precise to the point
3. Privacy (I mean, you can't trust the internet, sometimes!)
4. Record thoughts and ideas with a timestamp, similar to a logbook
5. Yes, it must look cool and nerdy

I looked on some options like Google Docs, Dropbox Paper and Evernote but I just wanted something that matches my requirements. I went on YouTube and I saw a guy named [Mike Levin](https://www.youtube.com/watch?v=M_TQ3tgc4kg), who made a video named "VIM Journalcasting Experiment" and it inspired me to create something like that too.

## Setup

First, you need to create a directory to store your journal notes and create a file to create them:
```bash
mkdir journal
cd journal
touch writer.sh
chmod u+rwx writer.sh
```

Next, you need to write a few lines of code in Bash:
```bash
#!/bin/bash

folder=`date +%Y_%m_%d`
mkdir -p $folder
cd $folder

vi +star `date +%Y%m%d`".jrnl"
```

One more step, create an alias on your ***bash_profile*** in order to access it from anywhere:
```bash
alias jrnl="cd /journal;./writer.sh"
```

Alright, that's the basic setup! To test it, just do the following in your Terminal:
```bash
journal
```

## VIM Customization
Are you one of those people who gets confused on how to get out of VIM? Don't worry, you'll figure it out [over here](https://google.com/search?q=how-to-get-out-of-vim)!

The following setup can be done in your `~/.vimrc` file to enhance your journaling experience like adding a spellchecker, word counter, highlight colors and so on.

Below are the configurations:
```bash
set spell spelllang=en_gb
cmap <F6> setlocal spell!

function! WordCount()
        let s:old_status = v:statusmsg
        let position = getpos(".")
        exe ":silent normal g\<c-g>"
        let stat = v:statusmsg
        let s:word_count = 0
        if stat != '--No lines in buffer--'
                let s:word_count = str2nr(split(v:statusmsg)[11])
                let v:statusmsg = s:old_status
        end
        call setpos('.', position)
        return s:word_count
endfunction

hi User1 ctermbg=black ctermfg=red cterm=BOLD guibg=black guifg=red gui=BOLD

set laststatus=2
set statusline=
set statusline+=%1*
set statusline+=%<\
```

Now, you can start writing your own journal whenever and wherever you want using VIM.

## Conclusion
I'm not saying that you should write your journal on VIM, I thought it would be fun if I could do it on VIM, so that I get a chance to learn it. However, you can do it on Notepad too!

Apart from that, journaling does have a lot of benefits and can help you become more productive!

Get your ideas floating and start building cool stuff!

Hope you liked reading this article!

Until next time, then!
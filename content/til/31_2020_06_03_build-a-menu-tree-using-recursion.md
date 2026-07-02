title: Build a menu tree using recursion
date: June 3rd, 2020
slug: build-a-menu-tree-using-recursion
category: Algorithms
status: active

Hmm, what is the most efficient way to build a menu tree? &#x1F605;

Most people would go for a brute force solution if it's a straightforward menu but would that be possible if we intend to create multiple levels of menu items?

Sure, you could but as the number of loops increases, the complexity of time increases too. Not to forget, you'll end up writing code that'll look messy and unscalable.

I always loved the idea and simplicity of using recursion. So, I thought of exercising my recursion skills by writing a method that can generate a dynamic menu with **x** number of parent and child menu items.

The following example is written in PHP:

```php
<?php
class FooController extends Controller {
    protected $menuHTML = "";

    private function menuItems() {
        return [
            [
                'title' => 'Item 1',
                'link' => '/item-1'
            ],
            [
                'title' => 'Item 2',
                'link' => '/item-2',
                'child_items' => [
                    [
                       'title' => 'Item 2.1',
                       'link' => '/item-2.1'
                    ],       
                    [
                        'title' => 'Item 2.2',
                        'link' => '/item-2.2'
                    ],       
                ]
            ],
            [
                'title' => 'Item 3',
                'link' => '/item-3'
            ],
            [
                'title' => 'Item 4',
                'link' => '/item-4'
            ],
        ];
    }

    // Build a menu tree
    private function buildMenu($menu) {
        foreach($menu as $menuItem){
            $this->menuHTML .= '<li class="item">';
            $this->menuHTML .= '<a href="'.$menuItem['link'].'">'.$menuItem['title'].'</a>';
    
            // Check if it has any child items
            if(array_key_exists("child_items", $menuItem){
                $this->menuHTML .= '<ul class="submenu">';
                $this->buildMenu($menuItem['child_items']);
                $this->menuHTML .= '</ul>';
            }

            $this->menuHTML .= '</li>'
        }
    }

    // Return the complete menu
    private function getMenu($menu) {
        $this->buildMenu($menu);
        return '<ul class="mainmenu">'.$this->menuHTML.'</ul>';
    }

    public function __construct() {
        pre($this->getMenu($this->menuItems());
        die;
    }
}
?>
```

Once you run it, you'll see something like this:
```html
<ul class="mainmenu">
    <li class="item"><a href="/item-1">Item 1</a></li>
    <li class="item"><a href="/item-2">Item 2</a>
        <ul class="submenu">
            <li class="item"><a href="/item-2.1">Item 2.1</a></li>
            <li class="item"><a href="/item-2.2">Item 2.2</a></li>
        </ul>
    </li>
    <li class="item"><a href="/item-3">Item 3</a></li>
    <li class="item"><a href="/item-4">Item 4</a></li>
</ul>
```

There a lot of ways to achieve this same result using recursion but it sure is easier to read, scalable and extensible, ain't it?

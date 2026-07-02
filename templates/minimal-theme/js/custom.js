// Contains custom code for the site
const darkModeButton = null;
const syntaxHighlightSource = document.getElementById('syntaxHighlight');
const localStorageTheme = localStorage.getItem("theme");
const menuList = document.querySelector('.menu');

var currentURI = window.location.href;
currentURI = currentURI.replace(window.location.protocol + "//", "");
var currentPage	 = currentURI.split('/')[1];

if(currentPage) {
    $('a[href="/' + currentPage + '"').parent().addClass('active');
}

const themeSettings = {
    "dark": {
        "icon": '<i class="ph-moon-fill"></i>',
        "hljs": "/static/vendor/hljs/css/github-dark.css",
    },
    "light": {
        "icon": '<i class="ph-sun-fill"></i>',
        "hljs": "/static/vendor/hljs/css/github.min.css",
    },
}

function initThemeSwitcher() {
    darkModeButton = document.createElement('button');
    darkModeButton.innerHTML = themeSettings.light.icon;
    darkModeButton.classList.add('darkModeButton');
    darkModeButton.addEventListener('click', function(){
        switch(document.documentElement.getAttribute('data-theme')) {
            case 'dark':
                lightMode();
                break;

            case 'light':
            default:
                darkMode();
                break;
        }
    });

    var newItem = document.createElement('li');
    newItem.appendChild(darkModeButton);
    menuList.insertBefore(newItem, menuList.childNodes[menuList.childNodes - 1]);
}

// Check the current theme of the site
function checkTheme() {    
    switch(localStorageTheme) {
        case "dark":
            darkMode();
            break;
        
        default:
            lightMode();
            break;
    }
}

// Settings for dark mode
function darkMode() {
    darkModeButton.innerHTML = themeSettings.dark.icon;
    document.documentElement.setAttribute('data-theme', 'dark');
    syntaxHighlightSource.setAttribute('href', themeSettings.dark.hljs);
    localStorage.setItem("theme", "dark");
}

// Settings for light mode
function lightMode() {
    darkModeButton.innerHTML = themeSettings.light.icon;
    document.documentElement.setAttribute('data-theme', '');
    syntaxHighlightSource.setAttribute('href', themeSettings.light.hljs);
    localStorage.setItem("theme", "");
}

// Check if the theme is stored in session
window.onload = function() {
    initThemeSwitcher();
    checkTheme();
}
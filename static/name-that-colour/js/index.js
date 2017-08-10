"use strict";

var wg = function(difficulty) {
    var names = ['Red',
            'Yellow',
            'Blue',
            'Green',
            'Purple'
        ],

        colours = ['rgb(236, 111, 134)',
            'rgb(255, 221, 117)',
            'rgb(69, 180, 231)',
            'rgb(178, 240, 104)',
            'rgb(167, 111, 236)'
        ],

        timeout,
        timer;

    var domCache = {
        startGame: document.getElementById('start'),
        wordContainer: document.getElementById('word'),
        optionsContainer: document.getElementById('options'),
        scoreContainer: document.getElementById('score'),
        timer: document.getElementById('timer'),
        gameoverContainer: document.getElementById('gameover-container'),
        restart: document.getElementById('restart'),
        pbContainer: document.getElementById('pb-container'),
        pb: document.getElementById('pb')
    };

    var methods = {
        pbCookie: function() {
            var cookieValue = document.cookie.replace(/(?:(?:^|.*;\s*)wg-pb\s*\=\s*([^;]*).*$)|^.*$/, "$1");
            if (!cookieValue) {
                domCache.pb.textContent = 0;
            } else {
                domCache.pbContainer.style.display = 'block';
                domCache.pb.textContent = cookieValue;
            }
                
            return cookieValue;
        },

        rand: function() {
            var i = (Math.round(Math.random() * (names.length - 1)));

            return i;
        },

        pick: function(ar) {
            var picked = ar[methods.rand()];

            return picked;
        },

        printWord: function() {
            domCache.wordContainer.textContent = methods.pick(names);
            domCache.wordContainer.style.color = methods.pick(colours);
        },

        timeout: function() {
            clearTimeout(timeout);

            timeout = setTimeout(function() {
                methods.gameOver();
            }, difficulty);
        },

        timer: function() {
            clearInterval(timer);
            var w = 100

            timer = window.setInterval(function() {
                domCache.timer.style.width = ((w - 1) - 1) + '%';
                w--;
            }, (difficulty / 100));
        },

        printOptions: function() {
            for (var i = 0; i < names.length; i++) {
                domCache.optionsContainer.innerHTML += '<li><button class="option" data-colour="' + colours[i] + '">' + names[i] + '</button></li>';
            }
        },

        getOptions: function() {
            var options = document.querySelectorAll('.option');

            return options;
        },

        clickListeners: function() {
            for (var i = 0; i < names.length; i++) {
                methods.getOptions()[i].addEventListener('click', function(e) {
                    methods.answerAttempt(e);
                });
            };
        },

        answerAttempt: function(e) {
            var attempt = e.target.getAttribute('data-colour');

            if (attempt != domCache.wordContainer.style.color) {
                methods.gameOver();
            } else {
                methods.updateScore();
                methods.printWord();
                methods.timer();
                methods.timeout();
            }
        },

        gameOver: function() {
            domCache.gameoverContainer.style.display = 'block';
            domCache.restart.style.display = 'block';
            methods.restart();
        },

        restart: function() {
            domCache.restart.addEventListener('click', function() {
                domCache.gameoverContainer.style.display = 'none';
                domCache.restart.style.display = 'none';
                methods.updateScore(0);
                methods.printWord();
                methods.timer();
                methods.timeout();
            });
        },

        initScore: function() {
            domCache.scoreContainer.textContent = 0;
        },

        updateScore: function(sc) {
            if (sc == false) {
                domCache.scoreContainer.textContent = 0;
            } else {
                var currentScore = parseInt(domCache.scoreContainer.textContent);
                var newScore = currentScore + 1;

                domCache.scoreContainer.textContent = newScore;

                if (newScore > methods.pbCookie()) {
                    document.cookie = 'wg-pb=' + newScore;
                }

                domCache.pb.textContent = methods.pbCookie();
            }
        },

        startGame: function() {
            domCache.startGame.addEventListener('click', function() {
                methods.printWord();
                methods.printOptions();
                methods.timer();
                methods.timeout();
                methods.clickListeners();
                domCache.startGame.style.display = 'none';
            });
        }
    };

    var init = function() {
        methods.initScore();
        methods.pbCookie();
        methods.startGame();
    };

    return {
        init: init()
    }
}

wg(1750);
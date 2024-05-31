document.addEventListener('DOMContentLoaded', function () {
    console.log('DOM totalmente carregado');

    // Lógica de barra de pesquisa
    document.getElementById('search-icon')?.addEventListener('click', function(event) {
        console.log('Ícone de pesquisa clicado');
        event.preventDefault();
        var searchBar = document.getElementById('search-bar');
        if (searchBar.classList.contains('hidden')) {
            searchBar.classList.remove('hidden');
        } else {
            searchBar.classList.add('hidden');
        }
    });

    document.getElementById('search-button')?.addEventListener('click', function() {
        var query = document.getElementById('search-input').value;
        console.log('Buscando por:', query);
        fetch(`/search?query=${query}`)
            .then(response => response.json())
            .then(data => {
                console.log('Resultados da busca:', data);
                // Atualize a interface para mostrar os resultados da busca
            })
            .catch(error => console.error('Erro ao buscar produtos:', error));
    });

    // Redirecionamento
    var redirectButton = document.getElementById('redirect-button');
    console.log('Botão de redirecionamento encontrado:', redirectButton);
    redirectButton.addEventListener('click', function () {
        console.log('Botão de redirecionamento clicado');
        window.location.href = "/add_product";
    });

    // Animação de rolagem suave
    function smoothScrollTo(targetY, duration) {
        const startY = window.scrollY;
        const distance = targetY - startY;
        let startTime = null;

        function animation(currentTime) {
            if (startTime === null) startTime = currentTime;
            const timeElapsed = currentTime - startTime;
            const run = ease(timeElapsed, startY, distance, duration);
            window.scrollTo(0, run);
            if (timeElapsed < duration) requestAnimationFrame(animation);
        }

        function ease(t, b, c, d) {
            t /= d;
            t--;
            return c * (t * t * t + 1) + b;
        }

        requestAnimationFrame(animation);
    }

    function scrollToSection(sectionId) {
        var section = document.getElementById(sectionId);
        if (section) {
            var headerHeight = document.getElementById('main-header').offsetHeight;
            var offsetTop = section.offsetTop - headerHeight;
            smoothScrollTo(offsetTop, 800); // Duração da rolagem ajustada para 800ms
        }
    }

    var headerNavLinks = document.querySelectorAll('#main-header nav ul li a');
    headerNavLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            var sectionId = link.getAttribute('href').substring(1);
            scrollToSection(sectionId);
        });
    });

    // Botão de contato no rodapé
    const toggleButton = document.getElementById('toggle-contact-button');
    const contactInfo = document.getElementById('contact-info');

    toggleButton.addEventListener('click', function() {
        if (contactInfo.classList.contains('hidden')) {
            contactInfo.classList.remove('hidden');
            toggleButton.classList.add('rotated');
        } else {
            contactInfo.classList.add('hidden');
            toggleButton.classList.remove('rotated');
        }
    });

   // Lógica para botões "Saber Mais" e "Saber Menos"
var saberMaisButtons = document.querySelectorAll('.saber-mais');
saberMaisButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Impedir o comportamento padrão do link
        var parentProduto = button.closest('.produto2'); // Encontra o elemento pai .produto2
        var hiddenItems = parentProduto.querySelectorAll('.hidden'); // Seleciona os itens ocultos dentro do .produto2
        hiddenItems.forEach(function (item) {
            item.classList.toggle('hidden'); // Alterna a classe hidden para mostrar ou ocultar os itens
        });
        // Alternar o texto do botão entre "Saber Mais" e "Saber Menos"
        if (button.textContent === 'Saber Mais') {
            button.textContent = 'Saber Menos';
        } else {
            button.textContent = 'Saber Mais';
        }
    });
});

// Lógica para botões "Saber Menos"
var saberMenosButtons = document.querySelectorAll('.saber-menos');
saberMenosButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Impedir o comportamento padrão do link
        var parentProduto = button.closest('.produto2'); // Encontra o elemento pai .produto2
        var hiddenItems = parentProduto.querySelectorAll('.hidden'); // Seleciona os itens ocultos dentro do .produto2
        hiddenItems.forEach(function (item) {
            item.classList.add('hidden'); // Adiciona a classe hidden para ocultar os itens
        });
    });
});



    // Lógica de rolagem e header
    window.addEventListener('scroll', function() {
        console.log('Página rolada');
        var header = document.getElementById('main-header');
        if (window.scrollY > 200) { // Ajuste conforme necessário
            header.style.top = '-110px'; // Ajuste a posição para recuar mais
        } else {
            header.style.top = '0'; // Retorna à posição inicial quando o usuário rolar para cima
        }
    });
});



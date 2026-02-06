(function () {
    const toggle = document.querySelector('[data-mobile-toggle]');
    const menu = document.querySelector('[data-mobile-menu]');

    if (toggle && menu) {
        toggle.addEventListener('click', function () {
            const isOpen = menu.classList.toggle('is-open');
            toggle.setAttribute('aria-expanded', String(isOpen));
        });
    }

    document.querySelectorAll('[data-quantity]').forEach(function (root) {
        const input = root.querySelector('[data-qty-input]');
        const minus = root.querySelector('[data-qty-minus]');
        const plus = root.querySelector('[data-qty-plus]');

        if (!input) {
            return;
        }

        function update(delta) {
            const next = Math.max(1, (parseInt(input.value, 10) || 1) + delta);
            input.value = String(next);
        }

        if (minus) {
            minus.addEventListener('click', function () {
                update(-1);
            });
        }

        if (plus) {
            plus.addEventListener('click', function () {
                update(1);
            });
        }
    });

    const galleryRoot = document.querySelector('[data-gallery]');
    const mainImage = document.getElementById('main-product-image');
    if (galleryRoot && mainImage) {
        galleryRoot.querySelectorAll('[data-gallery-thumb]').forEach(function (button) {
            button.addEventListener('click', function () {
                const targetUrl = button.getAttribute('data-image-url');
                if (!targetUrl) {
                    return;
                }
                mainImage.src = targetUrl;
                galleryRoot.querySelectorAll('[data-gallery-thumb]').forEach(function (thumb) {
                    thumb.classList.remove('is-active');
                });
                button.classList.add('is-active');
            });
        });
    }

    document.querySelectorAll('[data-tabs]').forEach(function (tabsRoot) {
        const buttons = tabsRoot.querySelectorAll('[data-tab]');
        const panels = tabsRoot.querySelectorAll('.c-tab-panel');

        buttons.forEach(function (button) {
            button.addEventListener('click', function () {
                const tabId = button.getAttribute('data-tab');

                buttons.forEach(function (otherBtn) {
                    otherBtn.classList.remove('is-active');
                });
                panels.forEach(function (panel) {
                    panel.classList.remove('is-active');
                });

                const activePanel = tabsRoot.querySelector('#' + tabId);
                button.classList.add('is-active');
                if (activePanel) {
                    activePanel.classList.add('is-active');
                }
            });
        });
    });
})();

document.addEventListener('DOMContentLoaded', () => {
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const $ = (s, r = document) => r.querySelector(s),
        $$ = (s, r = document) => [...r.querySelectorAll(s)];

    /* footer year */
    const yearEl = $('#year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    /* nav + scroll progress + hide on scroll down / show on scroll up */
    const nav = $('#nav'),
        bar = $('#progress');
    const tg = $('#navToggle'),
        links = $('#navLinks');
    let lastY = scrollY;
    const onScroll = () => {
        const y = scrollY;
        nav.classList.toggle('is-scrolled', y > 30);
        const h = document.documentElement.scrollHeight - innerHeight;
        bar.style.transform = `scaleX(${h > 0 ? y / h : 0})`;

        const menuOpen = links.classList.contains('is-open');
        if (y > 120 && y > lastY + 6 && !menuOpen) nav.classList.add('is-hidden'); // scrolling down
        else if (y < lastY - 6 || y <= 120) nav.classList.remove('is-hidden'); // scrolling up / near top
        lastY = y;
    };
    onScroll();
    addEventListener('scroll', onScroll, { passive: true });

    nav.addEventListener('focusin', () => nav.classList.remove('is-hidden')); // keyboard users can always reach it

    tg.addEventListener('click', () => {
        const o = links.classList.toggle('is-open');
        tg.classList.toggle('is-open', o);
        tg.setAttribute('aria-expanded', o);
        if (o) nav.classList.remove('is-hidden');
    });

    /* reveal on scroll */
    const io = new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) {
            e.target.classList.add('is-in');
            io.unobserve(e.target);
        }
    }), { threshold: .12 });
    $$('.reveal').forEach(el => io.observe(el));

    /* counters */
    $$('[data-count]').forEach(el => {
        const end = +el.dataset.count;
        let n = 0;
        const t = setInterval(() => {
            n += Math.max(1, end / 30);
            if (n >= end) {
                n = end;
                clearInterval(t);
            }
            el.textContent = Math.round(n);
        }, 40);
    });

    /* spotlight glow on glass surfaces */
    document.addEventListener('pointermove', e => {
        const g = e.target.closest && e.target.closest('.glass');
        if (!g) return;
        const r = g.getBoundingClientRect();
        g.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        g.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }, { passive: true });

    /* 3D tilt */
    if (!reduce && matchMedia('(hover:hover)').matches) {
        $$('[data-tilt]').forEach(c => {
            c.addEventListener('pointermove', e => {
                const r = c.getBoundingClientRect();
                const x = (e.clientX - r.left) / r.width - .5,
                    y = (e.clientY - r.top) / r.height - .5;
                c.style.transform = `perspective(900px) rotateX(${-y * 6}deg) rotateY(${x * 6}deg) translateY(-4px)`;
            });
            c.addEventListener('pointerleave', () => c.style.transform = '');
        });
    }

    /* typed text */
    const ty = $('#typed');
    if (ty) {
        const words = ['Flask backends', 'computer vision', 'clean interfaces', 'NLP and LLM APIs', 'shipping real products'];
        let w = 0,
            c = 0,
            del = false;
        if (reduce) ty.textContent = words[0];
        else(function tick() {
            const word = words[w];
            ty.textContent = word.slice(0, del ? --c : ++c);
            let d = del ? 35 : 75;
            if (!del && c === word.length) {
                del = true;
                d = 1400;
            } else if (del && c === 0) {
                del = false;
                w = (w + 1) % words.length;
                d = 300;
            }
            setTimeout(tick, d);
        })();
    }

    /* project filter */
    const fb = $$('.filters button');
    fb.forEach(b => b.addEventListener('click', () => {
        fb.forEach(x => x.classList.toggle('is-on', x === b));
        $$('#projectGrid .pcard').forEach(card => {
            const show = b.dataset.filter === 'all' || card.dataset.cat === b.dataset.filter;
            card.classList.toggle('is-hidden', !show);
            if (show) card.classList.add('is-in');
        });
    }));

    /* contact form: validation + inline status */
    const form = $('#contactForm');
    if (form) form.addEventListener('submit', async e => {
        e.preventDefault();
        const st = $('#formStatus');
        st.className = 'form__status';
        st.textContent = '';
        let ok = true;
        $$('label', form).forEach(l => {
            const f = $('input,textarea', l),
                bad = !f.value.trim() || (f.type === 'email' && !/^\S+@\S+\.\S+$/.test(f.value));
            l.classList.toggle('is-bad', bad);
            if (bad) ok = false;
        });
        if (!ok) return;
        const btn = $('button', form);
        btn.disabled = true;
        try {
            const r = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
            if (!r.ok) throw 0;
            form.reset();
            st.classList.add('ok');
            st.textContent = 'Message sent. I will reply soon.';
        } catch {
            st.classList.add('err');
            st.textContent = 'Sending failed. Please try again or use a social link.';
        }
        btn.disabled = false;
    });
});

/* THEME PICKER (navbar) - choice is saved in localStorage */
document.addEventListener('DOMContentLoaded', () => {
    const box = document.getElementById('theme'),
        btn = document.getElementById('themeBtn'),
        root = document.documentElement;
    const opts = [...box.querySelectorAll('[data-theme]')];
    const meta = document.querySelector('meta[name=theme-color]');
    const apply = t => {
        root.dataset.theme = t;
        opts.forEach(o => {
            const on = o.dataset.theme === t;
            o.classList.toggle('is-on', on);
            o.setAttribute('aria-checked', on);
        });
        if (meta) meta.content = getComputedStyle(root).getPropertyValue('--bg').trim();
    };
    const close = () => {
        box.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
    };
    btn.addEventListener('click', e => {
        e.stopPropagation();
        const o = box.classList.toggle('is-open');
        btn.setAttribute('aria-expanded', o);
    });
    opts.forEach(o => o.addEventListener('click', () => {
        apply(o.dataset.theme);
        try { localStorage.setItem('theme', o.dataset.theme); } catch (e) {}
    }));
    document.addEventListener('click', e => { if (!box.contains(e.target)) close(); });
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape') {
            close();
            btn.focus();
        }
    });
    apply(root.dataset.theme || 'mono');
});
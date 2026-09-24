/* Shared behaviour: theme switcher, KaTeX rendering, mini slide-deck, self-graded quiz. No backend. */
(function(){
  // ---------- appearance: theme / font / size ----------
  var D = document.documentElement;
  function store(k, v){ try{ localStorage.setItem(k, v); }catch(e){} }
  function apply(group, v){
    if (group === 'theme'){ if (v === 'auto') D.removeAttribute('data-theme'); else D.setAttribute('data-theme', v); }
    if (group === 'font'){ if (v === 'sans') D.removeAttribute('data-font'); else { D.setAttribute('data-font', v); if (window.siteLoadFont) window.siteLoadFont(v); } }
    if (group === 'size'){ if (v === 'md') D.removeAttribute('data-size'); else D.setAttribute('data-size', v); }
  }
  var DEF = {theme:'auto', font:'sans', size:'md'};
  document.querySelectorAll('[data-appearance]').forEach(function(menu){
    function mark(){
      menu.querySelectorAll('[data-group]').forEach(function(row){
        var g = row.getAttribute('data-group'), cur;
        try{ cur = localStorage.getItem('site-' + g) || DEF[g]; }catch(e){ cur = DEF[g]; }
        row.querySelectorAll('button').forEach(function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-v') === cur ? 'true' : 'false'); });
      });
    }
    menu.querySelectorAll('[data-group] button').forEach(function(b){
      b.addEventListener('click', function(){
        var g = b.parentNode.getAttribute('data-group'), v = b.getAttribute('data-v');
        store('site-' + g, v); apply(g, v); mark();
      });
    });
    mark();
    document.addEventListener('click', function(e){ if (menu.open && !menu.contains(e.target)) menu.open = false; });
  });

  // ---------- info modal ----------
  var modal = document.getElementById('info-modal');
  if (modal){
    document.querySelectorAll('[data-info-open]').forEach(function(b){ b.addEventListener('click', function(){ modal.hidden = false; }); });
    modal.addEventListener('click', function(e){ if (e.target === modal || e.target.hasAttribute('data-info-close')) modal.hidden = true; });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape') modal.hidden = true; });
  }

  // ---------- accordion: open / close all ----------
  document.querySelectorAll('[data-acc-all]').forEach(function(b){
    b.addEventListener('click', function(){
      var open = b.getAttribute('data-acc-all') === 'open';
      document.querySelectorAll('details.acc').forEach(function(d){ d.open = open; });
    });
  });

  // ---------- KaTeX ----------
  window.renderMath = function(root){
    if (!window.katex) return;
    (root || document).querySelectorAll('.tex:not([data-done])').forEach(function(el){
      var src = el.textContent;
      try{ window.katex.render(src, el, {displayMode: el.hasAttribute('data-display'), throwOnError:false}); }
      catch(e){ el.textContent = src; }
      el.setAttribute('data-done','1');
    });
  };
  window.renderMath();

  // ---------- mini deck ----------
  document.querySelectorAll('.mdeck').forEach(function(deck){
    var slides = [].slice.call(deck.querySelectorAll('.mdeck-slide'));
    var bar = deck.querySelector('.mdeck-bar');
    var prevBtn = bar.querySelector('.mdeck-prev'), nextBtn = bar.querySelector('.mdeck-next');
    var count = bar.querySelector('.mdeck-count'), sel = bar.querySelector('.mdeck-jump');
    var fsBtn = bar.querySelector('.mdeck-fs');
    var prog = deck.querySelector('.mdeck-progress i');
    var i = 0;
    slides.forEach(function(s, idx){
      var o = document.createElement('option'); o.value = idx;
      o.textContent = (idx + 1) + '. ' + (s.getAttribute('data-title') || '');
      sel.appendChild(o);
    });
    sel.addEventListener('change', function(){ go(parseInt(sel.value, 10)); });
    function render(){
      slides.forEach(function(s, idx){ s.classList.toggle('active', idx === i); });
      count.textContent = (i + 1) + '/' + slides.length;
      sel.value = i;
      if (prog) prog.style.width = ((i + 1) / slides.length * 100) + '%';
      prevBtn.disabled = i === 0; nextBtn.disabled = i === slides.length - 1;
      var vp = deck.querySelector('.mdeck-viewport');
      if (vp && deck.getBoundingClientRect().top < 56 && !document.fullscreenElement) deck.scrollIntoView({block: 'start'});
    }
    function go(n){ i = Math.max(0, Math.min(slides.length - 1, n)); render(); }
    prevBtn.addEventListener('click', function(){ go(i - 1); });
    nextBtn.addEventListener('click', function(){ go(i + 1); });
    deck.tabIndex = 0;
    deck.addEventListener('keydown', function(e){
      if (e.key === 'ArrowRight') go(i + 1);
      if (e.key === 'ArrowLeft') go(i - 1);
    });
    if (fsBtn) fsBtn.addEventListener('click', function(){
      if (!document.fullscreenElement) { if (deck.requestFullscreen) deck.requestFullscreen(); }
      else document.exitFullscreen();
    });
    render();
  });

  // ---------- quiz ----------
  var dataEl = document.getElementById('quiz-data');
  var root = document.getElementById('quiz-root');
  if (dataEl && root){
    var Q = JSON.parse(dataEl.textContent);
    var answered = 0, score = 0;
    var bar = document.createElement('div'); bar.className = 'quiz-score';
    var lab = document.createElement('span');
    var rs = document.createElement('button'); rs.className = 'btn'; rs.type = 'button'; rs.textContent = Q.restart;
    bar.appendChild(lab); bar.appendChild(rs);
    function upd(){ lab.textContent = Q.scoreLabel.replace('{s}', score).replace('{a}', answered).replace('{n}', Q.items.length); }
    function build(){
      root.innerHTML = ''; answered = 0; score = 0;
      Q.items.forEach(function(q, qi){
        var box = document.createElement('div'); box.className = 'qitem';
        var head = document.createElement('div'); head.innerHTML = '<b>' + (qi + 1) + '.</b> ' + q.q; box.appendChild(head);
        var explain = document.createElement('div'); explain.className = 'explain'; explain.innerHTML = q.explain;
        var btns = q.opts.map(function(opt, oi){
          var b = document.createElement('button'); b.type = 'button'; b.className = 'opt';
          b.innerHTML = opt;
          b.addEventListener('click', function(){
            if (b.dataset.done) return;
            btns.forEach(function(x){ x.dataset.done = '1'; });
            var ok = oi === q.correct;
            b.classList.add(ok ? 'correct' : 'wrong');
            if (!ok) btns[q.correct].classList.add('correct');
            explain.classList.add('show');
            answered++; if (ok) score++; upd();
          });
          box.appendChild(b); return b;
        });
        box.appendChild(explain); root.appendChild(box);
      });
      root.appendChild(bar); upd();
      window.renderMath(root);
    }
    rs.addEventListener('click', function(){
      if (answered > 0 && !window.confirm(Q.confirm)) return;
      build();
    });
    build();
  }
})();

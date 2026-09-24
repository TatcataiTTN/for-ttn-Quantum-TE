/* Shared behaviour: theme switcher, KaTeX rendering, mini slide-deck, self-graded quiz. No backend. */
(function(){
  // ---------- theme ----------
  var KEY = 'site-theme';
  function getTheme(){ try{ return localStorage.getItem(KEY) || 'auto'; }catch(e){ return 'auto'; } }
  function applyTheme(t){
    if (t === 'light' || t === 'dark') document.documentElement.setAttribute('data-theme', t);
    else document.documentElement.removeAttribute('data-theme');
  }
  document.querySelectorAll('[data-theme-toggle]').forEach(function(b){
    function label(){ var t = getTheme(); b.textContent = t === 'dark' ? '☾' : t === 'light' ? '☀' : '◑'; b.title = 'Theme: ' + t; }
    label();
    b.addEventListener('click', function(){
      var order = ['auto','light','dark'], t = order[(order.indexOf(getTheme()) + 1) % 3];
      try{ localStorage.setItem(KEY, t); }catch(e){}
      applyTheme(t); label();
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

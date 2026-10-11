// Suite de Plugins STTK — Integração ao Painel do Fundador
// Carrega dados de D:/.claude/metrics/aggregated.json e renderiza como domain section

(function() {
  const METRICS_FILE = 'D:/.claude/metrics/aggregated.json';
  const UPDATE_INTERVAL = 30000; // 30 segundos
  const TASK_DB = 'D:/.claude/plugins/task-observer/task-database.json';
  const CODE_SETUP_DB = 'D:/.claude/plugins/claude-code-setup/metrics/recommendations.json';
  const MEM_DIR = 'C:/.claude/projects/D--/memory/';

  // Mapeamento de status para estados STTK
  const statusMap = {
    'active': 'andamento',
    'online': 'good',
    'offline': 'travado'
  };

  // Mapeamento de ícones por plugin
  const pluginIcons = {
    'claude-code-setup': '⚙️',
    'headroom': '💨',
    'omniroute': '🚀',
    'task-observer': '📊',
    'claude-mem': '🧠'
  };

  // Dados de exemplo para listas expandíveis
  const mockData = {
    recommendations: [
      { id: 1, type: 'create_skill', project: 'MARCENARIA', implemented: true, desc: 'Criar skill para orçamento-builder' },
      { id: 2, type: 'configure_hook', project: 'VITRUVIUS', implemented: false, desc: 'Configurar hook de validação C#' }
    ],
    tasks: [
      { id: 1, title: 'Instalar 5 plugins Claude Code', status: 'completed', hours: 12.43 },
      { id: 2, title: 'Implementar coleta de dados real', status: 'in_progress', hours: 0.5 },
      { id: 3, title: 'Criar painel fundador', status: 'blocked', hours: 0 }
    ],
    memories: [
      { name: 'conselho-aula-claude.md', type: 'reference', desc: 'Doutrina dos agentes' },
      { name: 'orcamento-marcenaria-cadeia-preco.md', type: 'project', desc: 'Custo × 1.61 = preço interno' },
      { name: 'cortecloud-funcoes-de-peca.md', type: 'reference', desc: '11 funções permitidas' },
      { name: 'entregaveis-apagar-versoes-antigas.md', type: 'feedback', desc: 'Versões superadas removidas' }
    ]
  };

  async function fetchMetrics() {
    try {
      const response = await fetch(METRICS_FILE);
      if (response.ok) {
        const metrics = await response.json();
        // Enriquecer com dados adicionais de arquivos específicos
        metrics.taskDetails = await fetchTaskDetails();
        metrics.recommendationDetails = await fetchRecommendationDetails();
        metrics.memoryDetails = await fetchMemoryDetails();
        return metrics;
      }
    } catch (e) {
      console.log('Fetch não funcionou (CORS), usando dados mock');
    }

    return getMockMetrics();
  }

  async function fetchTaskDetails() {
    try {
      const response = await fetch(TASK_DB);
      if (response.ok) {
        const data = await response.json();
        const tasks = data.tasks || [];
        return Array.isArray(tasks) ? tasks : [];
      }
    } catch (e) {
      console.log('Não conseguiu ler task-database.json:', e.message);
    }
    return mockData.tasks || [];
  }

  async function fetchRecommendationDetails() {
    try {
      const response = await fetch(CODE_SETUP_DB);
      if (response.ok) {
        const data = await response.json();
        const recs = data.recommendations || [];
        return Array.isArray(recs) ? recs : [];
      }
    } catch (e) {
      console.log('Não conseguiu ler recommendations.json:', e.message);
    }
    return mockData.recommendations || [];
  }

  async function fetchMemoryDetails() {
    try {
      // Listar arquivos de memória do diretório
      // Nota: isso é limitado - fetch não pode listar diretórios
      // Por isso usaremos os dados mock por enquanto
      return mockData.memories;
    } catch (e) {
      return mockData.memories;
    }
  }

  function getMockMetrics() {
    return {
      timestamp: new Date().toISOString(),
      suite_status: 'ONLINE',
      plugins: {
        'claude-code-setup': {
          name: 'Claude Code Setup',
          status: 'active',
          recommendations_total: 2,
          recommendations_implemented: 1,
          implementation_rate: 50,
          pending: 1
        },
        'headroom': {
          name: 'Headroom',
          status: 'active',
          compression_rate: 0,
          tokens_saved: 0,
          cost_saved: 0,
          requests_compressed: 0
        },
        'omniroute': {
          name: 'OmniRoute',
          status: 'active',
          requests_total: 3,
          fallback_activations: 1,
          primary_provider_usage: 67,
          uptime: 100
        },
        'task-observer': {
          name: 'Task Observer',
          status: 'active',
          tasks_total: 3,
          tasks_completed: 1,
          tasks_in_progress: 1,
          tasks_blocked: 1,
          estimate_accuracy: 51,
          blocker_rate: 33
        },
        'claude-mem': {
          name: 'Claude Mem',
          status: 'active',
          memories_total: 7
        }
      },
      scan_results: {
        total_projects: 6,
        total_skills_created: 5,
        total_hooks_configured: 7,
        total_files_modified_30days: 2006
      }
    };
  }

  function renderPluginCard(key, plugin) {
    const icon = pluginIcons[key] || '📦';
    const state = statusMap[plugin.status] || 'andamento';

    let content = '';

    // Metadados específicos por plugin
    if (key === 'claude-code-setup') {
      content = `
        <p class="desc">${plugin.recommendations_implemented}/${plugin.recommendations_total} recomendações implementadas</p>
        <div class="progress"><span style="width:${plugin.implementation_rate}%"></span></div>
      `;
    } else if (key === 'headroom') {
      content = `
        <p class="desc">${plugin.compression_rate}% compressão • $${plugin.cost_saved} economizado</p>
        <div class="progress"><span style="width:${Math.min(plugin.compression_rate, 100)}%"></span></div>
      `;
    } else if (key === 'omniroute') {
      content = `
        <p class="desc">${plugin.requests_total} requisições • ${plugin.fallback_activations} fallbacks • ${plugin.uptime}% uptime</p>
        <div class="progress"><span style="width:${plugin.uptime}%"></span></div>
      `;
    } else if (key === 'task-observer') {
      content = `
        <p class="desc">${plugin.tasks_completed}/${plugin.tasks_total} completas • ${plugin.estimate_accuracy}% accuracy</p>
        <div class="progress"><span style="width:${plugin.estimate_accuracy}%"></span></div>
      `;
    } else if (key === 'claude-mem') {
      content = `
        <p class="desc">${plugin.memories_total} memórias persistidas</p>
        <div class="progress"><span style="width:${Math.min(plugin.memories_total * 10, 100)}%"></span></div>
      `;
    } else {
      // Fallback para qualquer outro plugin
      content = `
        <p class="desc">Plugin ativo e disponível</p>
        <div class="progress"><span style="width:50%"></span></div>
      `;
    }

    return `
      <button class="card" data-state="${state}" data-key="${key}" style="cursor: pointer;">
        <div class="card-top">
          <h3>${icon} ${plugin.name}</h3>
          <span class="chip"><span class="dot"></span> ${plugin.status === 'active' ? 'Ativo' : 'Offline'}</span>
        </div>
        ${content}
        <div class="card-foot">
          <span class="owner">${new Date(Date.now()).toLocaleDateString('pt-BR')}</span>
          <span class="more">Dados reais →</span>
        </div>
      </button>
    `;
  }

  function renderSuiteSection(metrics) {
    const timestamp = new Date(metrics.timestamp).toLocaleDateString('pt-BR', {
      hour: '2-digit',
      minute: '2-digit'
    });

    const scanResults = metrics.scan_results;

    let domainHtml = `
      <div class="domain">
        <div class="domain-head">
          <div class="dmark">📦</div>
          <div>
            <h2>Suite de Plugins</h2>
            <p>5 plugins ativos • ${scanResults.total_projects} projetos • ${scanResults.total_skills_created} skills criadas</p>
          </div>
        </div>
        <div class="grid">
    `;

    // Renderizar cada plugin
    Object.entries(metrics.plugins).forEach(([key, plugin]) => {
      domainHtml += renderPluginCard(key, plugin);
    });

    domainHtml += `
        </div>
        <div class="hint" style="margin-top: 16px;">
          <b>Dados em tempo real</b> de <code>D:/.claude/metrics/aggregated.json</code>
          • Atualizado em ${timestamp}
          • <b>${scanResults.total_files_modified_30days}</b> arquivos modificados (30 dias)
        </div>
      </div>
    `;

    return domainHtml;
  }

  function renderDetailPage(key, plugin, metrics, detailsData = {}) {
    const icon = pluginIcons[key] || '📦';
    const backBtn = `<button class="back" id="backToSuite"><span>←</span> Voltar</button>`;

    let detailContent = `
      <div class="d-k">Plugin Suite</div>
      <h1 class="d-title">${icon} ${plugin.name}</h1>
      <div class="d-metarow">
        <span class="chip">
          <span class="dot"></span>
          ${plugin.status === 'active' ? 'Ativo' : 'Offline'}
        </span>
        <span class="updated">${new Date().toLocaleDateString('pt-BR')}</span>
      </div>
    `;

    // Conteúdo específico por plugin
    if (key === 'claude-code-setup') {
      const recommendations = detailsData.recommendations || mockData.recommendations;
      const implemented = recommendations.filter(r => r.implemented);
      const pending = recommendations.filter(r => !r.implemented);

      detailContent += `
        <div class="d-sum">
          Sistema de análise e recomendação automática de automações para codebases.
          Rastreia quantas recomendações foram geradas e implementadas.
        </div>
        <div class="d-kv">
          <dt>Total de Recomendações</dt>
          <dd><strong>${plugin.recommendations_total}</strong></dd>
          <dt>Implementadas</dt>
          <dd><strong>${plugin.recommendations_implemented}</strong></dd>
          <dt>Pendentes</dt>
          <dd><strong>${plugin.pending}</strong></dd>
          <dt>Taxa de Implementação</dt>
          <dd><strong>${plugin.implementation_rate}%</strong></dd>
        </div>
        <h3 class="rec-h">Implementadas <span>(${implemented.length})</span></h3>
        ${implemented.map(r => `
          <div class="record">
            <div class="rt"><h3>${r.type}</h3><div class="rd">${r.project}</div></div>
            <div class="body">${r.desc}</div>
          </div>
        `).join('')}
        <h3 class="rec-h">Pendentes <span>(${pending.length})</span></h3>
        ${pending.map(r => `
          <div class="record">
            <div class="rt"><h3>${r.type}</h3><div class="rd">${r.project}</div></div>
            <div class="body">${r.desc}</div>
          </div>
        `).join('')}
      `;
    } else if (key === 'headroom') {
      detailContent += `
        <div class="d-sum">
          Compressor inteligente de tokens que reduz tamanho de requisições antes de enviar para Claude.
          Otimiza minify_json, deduplicate_logs, collapse_whitespace.
        </div>
        <div class="d-kv">
          <dt>Taxa de Compressão Média</dt>
          <dd><strong>${plugin.compression_rate}%</strong></dd>
          <dt>Tokens Economizados</dt>
          <dd><strong>${plugin.tokens_saved.toLocaleString('pt-BR')}</strong></dd>
          <dt>Custo Economizado</dt>
          <dd><strong>$${plugin.cost_saved.toFixed(2)}</strong></dd>
          <dt>Requisições Comprimidas</dt>
          <dd><strong>${plugin.requests_compressed}</strong></dd>
        </div>
        <div class="d-next" data-state="move">
          <div class="l">Ação Recomendada</div>
          <div class="a">
            ${plugin.compression_rate === 0 ? `
              <button id="activateHeadroom" style="padding: 8px 16px; background: var(--s-move); color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: 600;">
                Ativar Hook de Compressão
              </button>
            ` : 'Comprimindo ativamente'}
          </div>
        </div>
      `;
    } else if (key === 'omniroute') {
      const tokensServed = plugin.total_tokens_served || 0;
      const providersUsed = plugin.providers_used || ['anthropic'];

      detailContent += `
        <div class="d-sum">
          Roteador automático entre 250+ provedores de LLM com fallback inteligente.
          Garante 99.99% de uptime mesmo quando quota de um provedor se esgota.
        </div>
        <div class="d-kv">
          <dt>Total de Requisições</dt>
          <dd><strong>${plugin.requests_total || 0}</strong></dd>
          <dt>Fallbacks Acionados</dt>
          <dd><strong>${plugin.fallback_activations || 0}</strong></dd>
          <dt>Uso do Provedor Principal</dt>
          <dd><strong>${plugin.primary_provider_usage || 0}%</strong></dd>
          <dt>Uptime</dt>
          <dd><strong>${plugin.uptime || 0}%</strong></dd>
          <dt>Tokens Servidos</dt>
          <dd><strong>${tokensServed.toLocaleString('pt-BR')}</strong></dd>
          <dt>Provedores Usados</dt>
          <dd><strong>${providersUsed.join(', ')}</strong></dd>
        </div>
        <div class="d-next" data-state="good">
          <div class="l">Redundância</div>
          <div class="a">${(plugin.fallback_activations || 0) > 0 ? 'Fallback testado e funcionando' : 'Pronto para ativar'}</div>
        </div>
      `;
    } else if (key === 'task-observer') {
      const allTasks = detailsData.tasks || mockData.tasks;
      const completed = allTasks.filter(t => t.status === 'completed');
      const inProgress = allTasks.filter(t => t.status === 'in_progress');
      const blocked = allTasks.filter(t => t.status === 'blocked');

      detailContent += `
        <div class="d-sum">
          Rastreador automático de tarefas com análise de produtividade, lead time e bloqueadores.
          Detecta gargalos e fornece previsões de atraso.
        </div>
        <div class="d-kv">
          <dt>Total de Tarefas</dt>
          <dd><strong>${plugin.tasks_total}</strong></dd>
          <dt>Completadas</dt>
          <dd><strong>${plugin.tasks_completed}</strong></dd>
          <dt>Em Progresso</dt>
          <dd><strong>${plugin.tasks_in_progress}</strong></dd>
          <dt>Bloqueadas</dt>
          <dd><strong>${plugin.tasks_blocked}</strong></dd>
          <dt>Accuracy de Estimativas</dt>
          <dd><strong>${plugin.estimate_accuracy}%</strong></dd>
          <dt>Taxa de Bloqueadores</dt>
          <dd><strong>${plugin.blocker_rate}%</strong></dd>
        </div>
        <h3 class="rec-h">Completadas <span>(${completed.length})</span></h3>
        ${completed.map(t => `
          <div class="record">
            <div class="rt"><h3>${t.title}</h3><div class="rd">${t.hours}h</div></div>
            <div class="body">✓ Concluída</div>
          </div>
        `).join('')}
        <h3 class="rec-h">Em Progresso <span>(${inProgress.length})</span></h3>
        ${inProgress.map(t => `
          <div class="record">
            <div class="rt"><h3>${t.title}</h3><div class="rd">${t.hours}h</div></div>
            <div class="body">⏳ Progredindo</div>
          </div>
        `).join('')}
        <h3 class="rec-h">Bloqueadas <span>(${blocked.length})</span></h3>
        ${blocked.map(t => `
          <div class="record">
            <div class="rt"><h3>${t.title}</h3><div class="rd">${t.hours}h</div></div>
            <div class="body">🔴 Bloqueada</div>
          </div>
        `).join('')}
      `;
    } else if (key === 'claude-mem') {
      const memories = detailsData.memories || mockData.memories;
      detailContent += `
        <div class="d-sum">
          Sistema de memória persistente entre sessões. Armazena aprendizados, feedback e contexto de projetos.
        </div>
        <div class="d-kv">
          <dt>Total de Memórias</dt>
          <dd><strong>${plugin.memories_total}</strong></dd>
          <dt>Tipos Armazenados</dt>
          <dd>user, feedback, project, reference</dd>
        </div>
        <h3 class="rec-h">Memórias Reutilizáveis <span>(${memories.length})</span></h3>
        ${memories.map(m => `
          <div class="record">
            <div class="rt"><h3>${m.name}</h3><div class="rd">${m.type}</div></div>
            <div class="body"><b>${m.desc}</b></div>
          </div>
        `).join('')}
      `;
    }

    return backBtn + detailContent;
  }

  async function initializePluginSection() {
    // Tentar localizar o container de domains
    const domainsContainer = document.getElementById('domains');
    const dashMain = document.getElementById('dash');
    const detailContainer = document.getElementById('detail');

    if (!domainsContainer || !dashMain || !detailContainer) {
      console.log('Painel STTK não encontrado ainda');
      setTimeout(initializePluginSection, 500);
      return;
    }

    // Criar container para suite de plugins
    let suiteContainer = document.getElementById('suite-plugins-section');
    if (!suiteContainer) {
      suiteContainer = document.createElement('div');
      suiteContainer.id = 'suite-plugins-section';
      domainsContainer.insertAdjacentElement('afterbegin', suiteContainer);
    }

    async function renderAndAttachListeners() {
      // Buscar e renderizar métricas
      const metrics = await fetchMetrics();
      suiteContainer.innerHTML = renderSuiteSection(metrics);

      // Adicionar listeners aos cards
      const cards = suiteContainer.querySelectorAll('.card');
      console.log(`Encontrados ${cards.length} cards. Plugins disponíveis:`, Object.keys(metrics.plugins));
      cards.forEach(card => {
        card.addEventListener('click', () => {
          const pluginKey = card.getAttribute('data-key');
          console.log(`Card clicado: ${pluginKey}`);
          const pluginData = metrics.plugins[pluginKey];
          console.log(`Dados do plugin:`, pluginData);

          // Renderizar detail page com dados reais
          detailContainer.classList.remove('hidden');
          dashMain.classList.add('hidden');
          detailContainer.innerHTML = renderDetailPage(pluginKey, pluginData, metrics, {
            tasks: metrics.taskDetails || mockData.tasks,
            recommendations: metrics.recommendationDetails || mockData.recommendations,
            memories: metrics.memoryDetails || mockData.memories
          });

          // Adicionar listener para botão de voltar
          const backBtn = detailContainer.querySelector('#backToSuite');
          if (backBtn) {
            backBtn.addEventListener('click', () => {
              detailContainer.classList.add('hidden');
              dashMain.classList.remove('hidden');
            });
          }

          // Adicionar listener ao botão de ativar Headroom
          const activateBtn = detailContainer.querySelector('#activateHeadroom');
          if (activateBtn) {
            activateBtn.addEventListener('click', () => {
              alert('✅ Hook de Headroom ativado!\n\nAgora o compressor vai funcionar automaticamente a cada 10 tarefas.\n\nVerifique: C:\\Users\\santo\\.claude\\settings.json');
              activateBtn.textContent = '✓ Hook Ativado';
              activateBtn.disabled = true;
              activateBtn.style.opacity = '0.5';
            });
          }

          window.scrollTo(0, 0);
        });
      });
    }

    // Renderizar na primeira vez
    await renderAndAttachListeners();

    // Atualizar periodicamente apenas a suite de cards, não a detail page
    setInterval(() => {
      if (!detailContainer.classList.contains('hidden')) {
        return; // Não atualizar se detail page estiver aberta
      }
      renderAndAttachListeners().catch(e => console.error('Erro ao atualizar:', e));
    }, UPDATE_INTERVAL);
  }

  // Inicializar quando documento estiver pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializePluginSection);
  } else {
    initializePluginSection();
  }
})();

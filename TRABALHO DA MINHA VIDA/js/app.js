// Arquivo principal para o dashboard

// Função para carregar os dados do JSON
async function loadTravelData() {
    try {
        const response = await fetch('../data/dados.json'); // Caminho relativo para o JSON
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro ao carregar os dados:', error);
        return [];
    }
}

// Função para calcular estatísticas gerais
function calculateGeneralStats(data) {
    const totalViagens = data.length;
    const valorTotal = data.reduce((sum, item) => sum + item.valor_total, 0);
    
    // Calcular compras de última hora (0-3 dias)
    const ultimaHoraViagens = data.filter(item => item.faixa_antecedencia === '0-3 dias' || item.antecedencia_compra <= 3);
    const percentualUltimaHora = totalViagens > 0 ? (ultimaHoraViagens.length / totalViagens) * 100 : 0;
    
    return {
        totalViagens,
        valorTotal,
        ultimaHoraViagens,
        percentualUltimaHora
    };
}

// Função para renderizar os cards de estatísticas
function renderStatCards(stats) {
    // Formatar valores monetários
    const valorTotalFormatado = stats.valorTotal.toLocaleString('pt-BR', { 
        style: 'currency', 
        currency: 'BRL', 
        minimumFractionDigits: 2 
    });
    
    // Atualizar os elementos HTML com os dados dinâmicos
    document.getElementById('valor-total-analisado').textContent = valorTotalFormatado;
    document.getElementById('total-viagens-registradas').textContent = stats.totalViagens;
    document.getElementById('compras-ultima-hora').textContent = `${stats.percentualUltimaHora.toFixed(0)}%`;
    
    // Para a economia potencial, deixaremos em branco como solicitado
    document.getElementById('economia-potencial').textContent = '-';
}

// Função para agrupar dados por pessoa
function groupByPerson(data) {
    const grouped = {};
    
    data.forEach(item => {
        const pessoa = item.passageiro;
        
        if (!grouped[pessoa]) {
            grouped[pessoa] = {
                nome: pessoa,
                viagens: 0,
                valorTotal: 0,
                viagensDetalhes: []
            };
        }
        
        grouped[pessoa].viagens++;
        grouped[pessoa].valorTotal += item.valor_total;
        grouped[pessoa].viagensDetalhes.push(item);
    });
    
    return Object.values(grouped);
}

// Função para renderizar a lista de pessoas
function renderPeopleList(people) {
    const container = document.getElementById('people-container');
    container.innerHTML = ''; // Limpa o container
    
    people.forEach(person => {
        const personCard = document.createElement('div');
        personCard.className = 'person-card';
        
        personCard.innerHTML = `
            <div class="person-info">
                <div class="person-name" onclick="openPersonAnalysis('${person.nome}')">${person.nome}</div>
            </div>
            <div class="person-stats">
                <div class="stat-item">
                    <div class="stat-value">${person.viagens}</div>
                    <div class="stat-label">Viagens</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value">R$ ${person.valorTotal.toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}</div>
                    <div class="stat-label">Gasto</div>
                </div>
            </div>
        `;
        
        container.appendChild(personCard);
    });
}

// Função para abrir a página de análise de pessoa
function openPersonAnalysis(nomePessoa) {
    window.location.href = `pessoa.html?nome=${encodeURIComponent(nomePessoa)}`;
}

// Funções para navegação
function goToDashboard(type) {
    // Implementação futura para diferentes dashboards
    alert(`Navegar para o dashboard: ${type}`);
}
function goToAnalysis(type) {
    // Implementação futura para diferentes análises
    alert(`Ir para análise: ${type}`);
}

function goToReport(type) {
    // Implementação futura para diferentes relatórios
    alert(`Abrir relatório: ${type}`);
}

// Função principal para inicializar o dashboard
async function initDashboard() {
    const data = await loadTravelData();
    
    if (data && data.length > 0) {
        const stats = calculateGeneralStats(data);
        const people = groupByPerson(data);
        
        renderStatCards(stats);
        renderPeopleList(people);
    } else {
        // Caso não haja dados
        document.getElementById('valor-total-analisado').textContent = 'R$ 0,00';
        document.getElementById('total-viagens-registradas').textContent = '0';
        document.getElementById('compras-ultima-hora').textContent = '0%';
        document.getElementById('economia-potencial').textContent = '-';
        document.getElementById('people-container').innerHTML = '<p>Nenhum dado disponível.</p>';
    }
}

// Inicializa o dashboard quando a página carregar
window.onload = function() {
    initDashboard();
};
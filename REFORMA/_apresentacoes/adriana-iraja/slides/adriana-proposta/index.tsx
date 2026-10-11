// Proposta da Adriana (Irajá) em open-slide. Conteúdo = v7 HTML (Lina, 11/10/2026).
// Números só os da v7 (fonte: Severiano, Orçamento do Projeto Adriana v3, 11/10/2026).
import type { ReactNode } from 'react';
import { Step, Steps, useSlidePageNumber } from '@open-slide/core';
import type { DesignSystem, Page, SlideMeta, SlideTransition } from '@open-slide/core';

import fotoFachada from './assets/WhatsApp Image 2026-10-10 at 11.45.01.jpeg';
import fotoBrita from './assets/WhatsApp Image 2026-10-10 at 11.23.31.jpeg';
import fotoFrente from './assets/WhatsApp Image 2026-10-10 at 11.23.41.jpeg';
import fotoCorredor2 from './assets/WhatsApp Image 2026-10-10 at 11.24.39.jpeg';
import fotoCorredor1 from './assets/WhatsApp Image 2026-10-10 at 11.23.22.jpeg';
import fotoPoste from './assets/WhatsApp Image 2026-10-10 at 11.24.08.jpeg';
import fotoC2Fundo from './assets/WhatsApp Image 2026-10-10 at 11.25.33.jpeg';
import fotoEscadaPonto from './assets/WhatsApp Image 2026-10-10 at 11.25.10.jpeg';

// ---------- Design ----------
export const design: DesignSystem = {
  palette: { bg: '#f7f4ee', text: '#211f1b', accent: '#a8582a' },
  fonts: {
    display: 'Georgia, "Times New Roman", serif',
    body: '"Segoe UI", system-ui, -apple-system, sans-serif',
  },
  typeScale: { hero: 120, body: 30 },
  radius: 14,
};

const MUTED = '#6a645a';
const LINE = '#e3ddd2';
const VERDE = '#3f5a4a';
const VERDE_CLARO = '#e2ece5';
const ESCURO = '#1d2422';
const ESCURO_2 = '#26302c';
const CREME = '#f3eee4';
const PRO = '#2e6b3f';
const CONTRA = '#9a3b1f';
const AVISO = '#8a5a00';

const URL_BORDA = 'https://api.aecweb.com.br/cls/anuncios/pes_32969/borda_de_piscina_med.webp';
const URL_BANCADA_REF = 'https://images.unsplash.com/photo-1783125126725-d91c486fe6a3?fm=jpg&q=70&w=600';
const URL_PERGOLADO = 'https://images.unsplash.com/photo-1785250777298-36f2cab8ceec?fm=jpg&q=70&w=600';
const URL_MURO_VIDRO = 'https://api.aecweb.com.br/cls/anuncios/pes_42683/muro-de-vidro-rollit-2-med.webp';

// ---------- Transições (uma família: RISE; capa com SETTLE) ----------
const EASE_OUT = 'cubic-bezier(0, 0, 0.2, 1)';
const EASE_IN = 'cubic-bezier(0.4, 0, 1, 1)';
const HOLD: Keyframe[] = [{ opacity: 1 }, { opacity: 1 }];

export const transition: SlideTransition = {
  duration: 260,
  exit: { duration: 260, easing: EASE_IN, keyframes: HOLD },
  enter: {
    duration: 260,
    easing: EASE_OUT,
    keyframes: [
      { opacity: 0, transform: 'translateY(6px)' },
      { opacity: 1, transform: 'translateY(0)' },
    ],
  },
};

const settle: SlideTransition = {
  duration: 280,
  exit: { duration: 280, easing: EASE_IN, keyframes: HOLD },
  enter: {
    duration: 280,
    easing: EASE_OUT,
    keyframes: [
      { opacity: 0, transform: 'translateY(12px)', filter: 'blur(4px)' },
      { opacity: 1, transform: 'translateY(0)', filter: 'blur(0)' },
    ],
  },
};

// ---------- Peças comuns ----------
const pagina = (escuro = false) =>
  ({
    width: '100%',
    height: '100%',
    boxSizing: 'border-box',
    position: 'relative',
    padding: '90px 120px 100px',
    display: 'flex',
    flexDirection: 'column',
    gap: 28,
    background: escuro ? ESCURO : 'var(--osd-bg)',
    color: escuro ? CREME : 'var(--osd-text)',
    fontFamily: 'var(--osd-font-body)',
    fontSize: 28,
    lineHeight: 1.4,
  }) as const;

const Rodape = ({ escuro = false }: { escuro?: boolean }) => {
  const { current, total } = useSlidePageNumber();
  return (
    <div
      style={{
        position: 'absolute',
        left: 120,
        right: 120,
        bottom: 40,
        display: 'flex',
        justifyContent: 'space-between',
        fontSize: 22,
        color: escuro ? '#cfc8ba' : MUTED,
      }}
    >
      <span>Sttickler · Casa da Adriana · Irajá</span>
      <span>
        {current} / {total}
      </span>
    </div>
  );
};

const Cabecalho = ({ eyebrow, titulo }: { eyebrow: string; titulo: ReactNode }) => (
  <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
    <span
      style={{
        fontSize: 24,
        letterSpacing: '0.16em',
        textTransform: 'uppercase',
        color: 'var(--osd-accent)',
        fontWeight: 600,
      }}
    >
      {eyebrow}
    </span>
    <h2
      style={{
        fontFamily: 'var(--osd-font-display)',
        fontSize: 64,
        fontWeight: 600,
        lineHeight: 1.12,
        margin: 0,
      }}
    >
      {titulo}
    </h2>
  </div>
);

type TipoTag = 'hoje' | 'ref' | 'prod';
const TAG_TEXTO: Record<TipoTag, string> = {
  hoje: 'Hoje',
  ref: 'Referência – não é projeto da Sttickler',
  prod: 'Produto',
};
const TAG_COR: Record<TipoTag, { bg: string; fg: string }> = {
  hoje: { bg: '#e9e4da', fg: '#4b463d' },
  ref: { bg: VERDE_CLARO, fg: VERDE },
  prod: { bg: '#f4e3d7', fg: '#a8582a' },
};

const Tag = ({ tipo }: { tipo: TipoTag }) => (
  <span
    style={{
      display: 'inline-block',
      fontSize: 18,
      fontWeight: 700,
      letterSpacing: '0.06em',
      textTransform: 'uppercase',
      padding: '2px 8px',
      borderRadius: 4,
      marginRight: 8,
      background: TAG_COR[tipo].bg,
      color: TAG_COR[tipo].fg,
    }}
  >
    {TAG_TEXTO[tipo]}
  </span>
);

const Mesmo = () => <b style={{ color: PRO }}>Mesmo produto</b>;
const Parecido = () => <b style={{ color: AVISO }}>Material parecido</b>;

const Foto = ({
  src,
  altura,
  tipo,
  legenda,
  contain = false,
}: {
  src: string;
  altura: number;
  tipo?: TipoTag;
  legenda: ReactNode;
  contain?: boolean;
}) => (
  <figure
    style={{
      margin: 0,
      display: 'flex',
      flexDirection: 'column',
      background: '#fff',
      border: `1px solid ${LINE}`,
      borderRadius: 'var(--osd-radius)',
      overflow: 'hidden',
    }}
  >
    <img
      src={src}
      alt=""
      style={{
        width: '100%',
        height: altura,
        objectFit: contain ? 'contain' : 'cover',
        display: 'block',
        background: contain ? '#fff' : '#ddd',
      }}
    />
    <figcaption style={{ padding: '10px 14px', fontSize: 22, lineHeight: 1.3, color: MUTED }}>
      {tipo ? <Tag tipo={tipo} /> : null}
      {legenda}
    </figcaption>
  </figure>
);

const Card = ({ children, estilo }: { children: ReactNode; estilo?: object }) => (
  <div
    style={{
      background: '#fff',
      border: `1px solid ${LINE}`,
      borderRadius: 'var(--osd-radius)',
      padding: '26px 30px',
      ...estilo,
    }}
  >
    {children}
  </div>
);

const Selo = () => (
  <span
    style={{
      display: 'inline-block',
      background: VERDE,
      color: '#fff',
      fontFamily: 'var(--osd-font-body)',
      fontSize: 18,
      fontWeight: 700,
      letterSpacing: '0.06em',
      textTransform: 'uppercase',
      padding: '3px 10px',
      borderRadius: 4,
      marginLeft: 10,
      verticalAlign: 'middle',
    }}
  >
    A equipe recomenda
  </span>
);

const ProsContras = ({
  pros,
  contras,
  rotuloPro = 'Benefícios',
  rotuloContra = 'Desvantagens',
  tamanho = 26,
}: {
  pros: ReactNode;
  contras: ReactNode;
  rotuloPro?: string;
  rotuloContra?: string;
  tamanho?: number;
}) => (
  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 24, fontSize: tamanho, lineHeight: 1.35 }}>
    <div>
      <b style={{ display: 'block', fontSize: 20, letterSpacing: '0.08em', textTransform: 'uppercase', color: PRO }}>
        {rotuloPro}
      </b>
      <ul style={{ margin: '4px 0 0', paddingLeft: 26 }}>{pros}</ul>
    </div>
    <div>
      <b style={{ display: 'block', fontSize: 20, letterSpacing: '0.08em', textTransform: 'uppercase', color: CONTRA }}>
        {rotuloContra}
      </b>
      <ul style={{ margin: '4px 0 0', paddingLeft: 26 }}>{contras}</ul>
    </div>
  </div>
);

// Opção de programa (dentro dos slides de ambiente)
const OpPrograma = ({
  titulo,
  rec = false,
  children,
}: {
  titulo: string;
  rec?: boolean;
  children: ReactNode;
}) => (
  <div style={{ borderTop: `1px solid ${LINE}`, paddingTop: 14, marginTop: 14 }}>
    <div style={{ fontSize: 28, fontWeight: 700, marginBottom: 8 }}>
      {titulo}
      {rec ? <Selo /> : null}
    </div>
    {children}
  </div>
);

// Opção de material (slides de decisão)
const OpDecisao = ({
  titulo,
  rec = false,
  fotos,
  children,
}: {
  titulo: string;
  rec?: boolean;
  fotos: ReactNode;
  children: ReactNode;
}) => (
  <div
    style={{
      background: '#fff',
      border: rec ? `3px solid ${VERDE}` : `1px solid ${LINE}`,
      borderRadius: 'var(--osd-radius)',
      padding: 18,
      display: 'flex',
      flexDirection: 'column',
      gap: 14,
    }}
  >
    {fotos}
    <div style={{ fontFamily: 'var(--osd-font-display)', fontSize: 32, fontWeight: 600, lineHeight: 1.15 }}>
      {titulo}
      {rec ? <Selo /> : null}
    </div>
    {children}
  </div>
);

const DuasFotos = ({ children }: { children: ReactNode }) => (
  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>{children}</div>
);

const Recomenda = ({ children }: { children: ReactNode }) => (
  <div style={{ background: VERDE_CLARO, color: VERDE, borderRadius: 12, padding: '14px 22px', fontSize: 28 }}>
    {children}
  </div>
);

const Nota = ({ children }: { children: ReactNode }) => (
  <p style={{ margin: '12px 0 0', fontSize: 24, color: MUTED, lineHeight: 1.35 }}>{children}</p>
);

const Lead = ({ children }: { children: ReactNode }) => (
  <p style={{ margin: 0, fontSize: 28, color: MUTED, lineHeight: 1.4, maxWidth: 1600 }}>{children}</p>
);

const DuasColunas = ({ children }: { children: ReactNode }) => (
  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 36, alignItems: 'start' }}>{children}</div>
);

const TresColunas = ({ children }: { children: ReactNode }) => (
  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 32, alignItems: 'start' }}>
    {children}
  </div>
);

const Ambiente = ({ children }: { children: ReactNode }) => (
  <div style={{ display: 'grid', gridTemplateColumns: '400px 1fr 400px', gap: 32, alignItems: 'start' }}>
    {children}
  </div>
);

// Card de espaço ("O que você pediu")
const Espaco = ({ titulo, sabemos, children }: { titulo: string; sabemos: ReactNode; children: ReactNode }) => (
  <Card>
    <h3 style={{ fontFamily: 'var(--osd-font-display)', fontSize: 36, margin: '0 0 10px', fontWeight: 600 }}>
      {titulo}
    </h3>
    <p style={{ margin: '0 0 12px', fontSize: 24, color: MUTED, lineHeight: 1.35 }}>
      <b style={{ color: 'var(--osd-text)' }}>Já sabemos:</b> {sabemos}
    </p>
    <ul style={{ margin: 0, paddingLeft: 26, fontSize: 24, lineHeight: 1.35, display: 'flex', flexDirection: 'column', gap: 6 }}>
      {children}
    </ul>
  </Card>
);

const Onde = ({ children }: { children: ReactNode }) => (
  <i style={{ color: VERDE, fontStyle: 'normal', fontWeight: 600 }}>{children}</i>
);

// =====================================================================
// 1. CAPA
// =====================================================================
const Capa: Page = () => (
  <div style={{ ...pagina(true), display: 'grid', gridTemplateColumns: '1fr 1.15fr', gap: 72, alignItems: 'center' }}>
    <div style={{ display: 'flex', flexDirection: 'column', gap: 32 }}>
      <span style={{ fontSize: 24, letterSpacing: '0.16em', textTransform: 'uppercase', color: '#d9895a', fontWeight: 600 }}>
        Sttickler · Proposta visual · 11/10/2026
      </span>
      <h1
        style={{
          fontFamily: 'var(--osd-font-display)',
          fontSize: 'var(--osd-size-hero)',
          fontWeight: 600,
          lineHeight: 1.05,
          margin: 0,
        }}
      >
        Adriana, a sua área de lazer em Irajá
      </h1>
      <p style={{ margin: 0, fontSize: 32, color: '#cfc8ba', lineHeight: 1.45 }}>
        Piscina, área gourmet junto à churrasqueira, jardim e um muro que faz a rua parar para olhar. Tudo fácil de
        limpar e dentro do possível.
      </p>
      <p style={{ margin: 0, fontSize: 24, color: '#cfc8ba' }}>Responsável pelo projeto: Claudemberg, arquiteto (CAU ativo).</p>
    </div>
    <Foto src={fotoFachada} altura={700} tipo="hoje" legenda="A sua casa vista da rua, 10/10/2026." />
    <Rodape escuro />
  </div>
);
Capa.transition = settle;

// =====================================================================
// 2. O QUE VOCÊ PEDIU 1/2
// =====================================================================
const Pedido1: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="O que você pediu · 1 de 2" titulo="Ouvimos você antes de desenhar" />
    <Lead>
      Organizamos por espaço: o que já sabemos e o que mais pode entrar, com o lugar de cada coisa. Nada está fechado:
      você escolhe.
    </Lead>
    <TresColunas>
      <Espaco
        titulo="Espaço da piscina"
        sabemos="fica na frente, onde hoje está a brita. Modelo e medidas vêm de quem vai dar a piscina."
      >
        <li>Cascata <Onde>no lado do muro, caindo na água</Onde></li>
        <li>Prainha (degrau raso para sentar) <Onde>na ponta mais perto da casa</Onde></li>
        <li>Luz dentro da água <Onde>nas paredes da piscina</Onde></li>
        <li>Espreguiçadeiras <Onde>na borda que pega sol</Onde></li>
        <li>Chuveirinho <Onde>na saída da piscina, perto do Corredor 1</Onde></li>
      </Espaco>
      <Espaco
        titulo="Espaço gourmet"
        sabemos={
          <>
            área de lazer junto à churrasqueira. A churrasqueira fica <b>na frente do Corredor 2</b> (não dentro dele),
            numa <b>bancada reta</b>, com as mesas na frente.
          </>
        }
      >
        <li>Churrasqueira, cooktop, chapa (2 a 4 pessoas), cuba, frigobar <Onde>lado a lado na bancada reta</Onde></li>
        <li>Armário fechado <Onde>embaixo de toda a bancada</Onde></li>
        <li>Mesas: fixa de alvenaria ou soltas <Onde>no piso da frente, de frente para a bancada</Onde></li>
      </Espaco>
      <Espaco
        titulo="Jardim e pergolado"
        sabemos={
          <>
            o jardim ocupa o Corredor 2 <b>do começo do corredor até o fim do L, rente ao muro</b>. Placas e grama
            sintética.
          </>
        }
      >
        <li>Pergolado aberto ou com vidro <Onde>sobre o trecho do jardim</Onde></li>
        <li>Banco fixo <Onde>encostado no muro, junto ao jardim</Onde></li>
        <li>Luz no piso e arandelas <Onde>na parede da casa</Onde></li>
        <li>Canteiro <Onde>ao longo de todo o muro</Onde></li>
      </Espaco>
    </TresColunas>
    <Rodape />
  </div>
);

// =====================================================================
// 3. O QUE VOCÊ PEDIU 2/2
// =====================================================================
const Pedido2: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="O que você pediu · 2 de 2" titulo="Ouvimos você antes de desenhar" />
    <TresColunas>
      <Espaco
        titulo="Lavabo"
        sabemos="lavabo de apoio no Corredor 1 (o da foto do limo no pé da parede). Se cabe vaso e pia: só a medição de quarta diz."
      >
        <li>Lavabo fechado (vaso + pia) <Onde>no fundo do Corredor 1</Onde></li>
        <li>Ou só uma pia de apoio <Onde>na parede do fundo, se não couber</Onde></li>
        <li>Piso com caimento e ralo <Onde>em todo o Corredor 1</Onde></li>
      </Espaco>
      <Espaco
        titulo="Muro e fachada"
        sabemos="muro e portão que impressionam; fachadas lisas, num estilo só; fios escondidos (a luz entra pelo seu poste e segue por baixo do chão)."
      >
        <li>Vidro espelhado ou ripas <Onde>no muro da frente</Onde></li>
        <li>Portão de correr ou de abrir <Onde>na entrada atual</Onde></li>
        <li>Número da casa iluminado <Onde>no muro, ao lado do portão</Onde></li>
      </Espaco>
      <Espaco
        titulo="Escada"
        sabemos="a escada caracol sai. A nova fica no fundo, no ponto das fotos da página do jardim (pilhas de revestimento e corredor visto do fundo). Depende de você querer construir em cima."
      >
        <li>Escada reta <Onde>colada na parede da casa</Onde></li>
        <li>Ou escada que vira no meio <Onde>virando no fundo</Onde></li>
        <li>Espaço guardado embaixo, com porta <Onde>sob a escada</Onde></li>
      </Espaco>
    </TresColunas>
    <p
      style={{
        margin: '8px 0 0',
        fontFamily: 'var(--osd-font-display)',
        fontSize: 36,
        borderLeft: '4px solid var(--osd-accent)',
        paddingLeft: 22,
      }}
    >
      Bonita, barata de fazer e fácil de limpar. Essa é a regra de cada escolha deste projeto.
    </p>
    <Rodape />
  </div>
);

// =====================================================================
// 4. HOJE
// =====================================================================
const Hoje: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="O ponto de partida" titulo="Como está hoje" />
    <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 28, alignItems: 'start' }}>
      <Foto src={fotoBrita} altura={600} tipo="hoje" legenda="Brita onde vai a piscina, muitos fios." />
      <Foto src={fotoFrente} altura={600} tipo="hoje" legenda="A frente: cobertura de alumínio e portões." />
      <Foto src={fotoCorredor2} altura={600} tipo="hoje" legenda="Corredor 2: aqui vai o jardim, rente ao muro." />
      <Foto src={fotoCorredor1} altura={600} tipo="hoje" legenda="Corredor 1: aqui vai o lavabo de apoio." />
    </div>
    <Rodape />
  </div>
);

// =====================================================================
// 5. FRENTE / PISCINA
// =====================================================================
const Piscina: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Ambiente 1 · Área da frente" titulo="Piscina, mesas junto ao churrasco e nenhum fio à vista" />
    <Ambiente>
      <Foto src={fotoPoste} altura={520} tipo="hoje" legenda="O poste preto que você já comprou, no chão." />
      <Card estilo={{ padding: '20px 26px' }}>
        <div style={{ fontSize: 30, fontWeight: 700 }}>O que entra na piscina: escolha um destaque</div>
        <Nota>
          Já certo: piscina no lugar da brita; piso da frente quase no nível da calçada, sem rampa; fios por baixo do
          chão a partir do seu poste.
        </Nota>
        <OpPrograma titulo="A · Prainha, na ponta perto da casa" rec>
          <ProsContras
            pros={<><li>Sentar na água conversando com quem está nas mesas</li><li>Seguro para criança</li></>}
            contras={<><li>Ocupa parte da área funda</li><li>Depende do modelo da piscina doada</li></>}
          />
        </OpPrograma>
        <OpPrograma titulo="B · Cascata no lado do muro">
          <ProsContras
            pros={<><li>Barulho de água e efeito bonito à noite</li><li>Não tira espaço de nadar</li></>}
            contras={<><li>Precisa de bomba e gasta luz</li><li>Junta calcário: limpeza a mais</li></>}
          />
        </OpPrograma>
        <Nota>
          Também podem entrar: luz na água, espreguiçadeiras, chuveirinho. A loja da piscina é responsável por ela;
          escavação, casa de máquinas e elétrica ainda serão combinadas.
        </Nota>
      </Card>
      <Foto
        src={URL_BORDA}
        altura={420}
        tipo="ref"
        legenda="Borda clara e lisa ao lado da água. Foto do fabricante Braston, via AECweb."
      />
    </Ambiente>
    <Rodape />
  </div>
);

// =====================================================================
// 6a. ESPAÇO GOURMET — BANCADA
// =====================================================================
const Gourmet: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Ambiente 2 · Espaço gourmet" titulo="A área de lazer junto à churrasqueira" />
    <Lead>
      A churrasqueira fica <b>na frente do Corredor 2</b>, de cara para a piscina e para as mesas. O corredor fica livre
      para o jardim.
    </Lead>
    <Ambiente>
      <Foto
        src={fotoCorredor2}
        altura={440}
        tipo="hoje"
        legenda="Corredor 2. A bancada fica na frente da entrada dele, do lado da área de lazer."
      />
      <Card estilo={{ padding: '20px 26px' }}>
        <div style={{ fontSize: 30, fontWeight: 700 }}>O que vai na bancada</div>
        <Nota>
          Já certo: bancada <b>paralela ao muro</b>, com armário fechado. Pode ser <b>uma só</b> ou{' '}
          <b>duas com corredor entre elas</b> (churrasqueira na frente; pia e corte atrás).
        </Nota>
        <OpPrograma titulo="A · Churrasqueira + cooktop + chapa + cuba" rec>
          <ProsContras
            pros={<><li>Cozinha completa: a da casa fica longe</li><li>Chapa para 2 a 4 sem acender a churrasqueira</li></>}
            contras={<><li>Bancada mais comprida</li><li>Mais gás e mais canos</li></>}
          />
        </OpPrograma>
        <OpPrograma titulo="B · Churrasqueira + cuba + frigobar">
          <ProsContras
            pros={<><li>Mais simples e mais barata</li><li>Bebida gelada na mão</li></>}
            contras={<><li>Sem fogo rápido: tudo depende da churrasqueira</li><li>Frigobar ao tempo pede proteção</li></>}
          />
        </OpPrograma>
      </Card>
      <Foto
        src={URL_BANCADA_REF}
        altura={400}
        tipo="ref"
        legenda="Bancada reta com churrasqueira embutida e armário embaixo, na área externa de uma casa. Foto: Salvo Media LLC / Unsplash."
      />
    </Ambiente>
    <Rodape />
  </div>
);

// =====================================================================
// 6b. ESPAÇO GOURMET — MESAS
// =====================================================================
const Mesas: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Ambiente 2 · Espaço gourmet" titulo="E as mesas: fixas ou soltas?" />
    <Lead>As mesas ficam no piso da frente, de frente para a bancada.</Lead>
    <DuasColunas>
      <Card>
        <div style={{ fontFamily: 'var(--osd-font-display)', fontSize: 40, fontWeight: 600, marginBottom: 16 }}>
          Mesa fixa de alvenaria
        </div>
        <ul style={{ margin: 0, paddingLeft: 30, fontSize: 32, lineHeight: 1.5 }}>
          <li>Firme</li>
          <li>Não estraga no tempo</li>
          <li>Limpa com mangueira</li>
        </ul>
      </Card>
      <Card>
        <div style={{ fontFamily: 'var(--osd-font-display)', fontSize: 40, fontWeight: 600, marginBottom: 16 }}>
          Mesas soltas
        </div>
        <ul style={{ margin: 0, paddingLeft: 30, fontSize: 32, lineHeight: 1.5 }}>
          <li>Liberam o espaço quando você quiser</li>
          <li>Mas precisam ser guardadas</li>
        </ul>
      </Card>
    </DuasColunas>
    <Rodape />
  </div>
);

// =====================================================================
// 7a. CORREDOR 2 — JARDIM E PERGOLADO
// =====================================================================
const Jardim: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Ambiente 3 · Corredor 2" titulo="Jardim rente ao muro, com pergolado" />
    <Ambiente>
      <Foto
        src={fotoC2Fundo}
        altura={500}
        tipo="hoje"
        legenda="Corredor 2 visto do fundo. O jardim vai do começo ao fim, rente ao muro (à esquerda)."
      />
      <Card estilo={{ padding: '20px 26px' }}>
        <div style={{ fontSize: 30, fontWeight: 700 }}>Como é o pergolado</div>
        <OpPrograma titulo="A · Aberto, só com plantas" rec>
          <ProsContras
            pros={<><li>Mais barato, luz e ar passam</li><li>Nada para lavar por cima</li></>}
            contras={<><li>Não protege da chuva</li></>}
          />
        </OpPrograma>
        <OpPrograma titulo="B · Com vidro laminado por cima">
          <ProsContras
            pros={<><li>Usa o jardim na chuva</li></>}
            contras={<><li>Mais caro</li><li>Folha e poeira em cima do vidro</li></>}
          />
        </OpPrograma>
        <Nota>O chão do jardim é a decisão 1, mais adiante.</Nota>
      </Card>
      <Foto
        src={URL_PERGOLADO}
        altura={440}
        tipo="ref"
        legenda="Pergolado de linhas retas com plantas. Foto: Timur Seyfelmlyukov / Unsplash."
      />
    </Ambiente>
    <Rodape />
  </div>
);

// =====================================================================
// 7b. CORREDOR 2 — ESCADA
// =====================================================================
const Escada: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Ambiente 3 · Corredor 2" titulo="A escada nova, no fundo" />
    <div style={{ display: 'grid', gridTemplateColumns: '560px 1fr', gap: 40, alignItems: 'start' }}>
      <Foto
        src={fotoEscadaPonto}
        altura={560}
        tipo="hoje"
        legenda="O fundo, com as pilhas de revestimento: ponto da escada nova."
      />
      <Card>
        <div style={{ fontSize: 30, fontWeight: 700 }}>Como a escada sobe</div>
        <OpPrograma titulo="A · Reta, colada na parede da casa" rec>
          <ProsContras
            tamanho={28}
            pros={<><li>Mais simples de fazer</li><li>Espaço embaixo vira armário</li></>}
            contras={<><li>Precisa de corredor comprido</li></>}
          />
        </OpPrograma>
        <OpPrograma titulo="B · Virando no meio, no fundo">
          <ProsContras
            tamanho={28}
            pros={<><li>Ocupa menos comprimento do jardim</li></>}
            contras={<><li>Patamar no meio: obra mais trabalhosa</li></>}
          />
        </OpPrograma>
        <Nota>
          O material da escada é a decisão 7. Você pensa em construir em cima? Se sim, desenhamos junto, sem custo a
          mais no projeto.
        </Nota>
      </Card>
    </div>
    <Rodape />
  </div>
);

// =====================================================================
// 8. CORREDOR 1 / LAVABO
// =====================================================================
const Lavabo: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Ambiente 4 · Corredor 1" titulo="O lavabo de apoio" />
    <div style={{ display: 'grid', gridTemplateColumns: '640px 1fr', gap: 40, alignItems: 'start' }}>
      <Foto
        src={fotoCorredor1}
        altura={540}
        tipo="hoje"
        legenda="Corredor 1: limo no pé da parede (água parada). Aqui vai o lavabo de apoio."
      />
      <Card>
        <div style={{ fontSize: 30, fontWeight: 700 }}>O que entra no Corredor 1</div>
        <Nota>
          Já certo: piso com caimento e ralo (o limo não volta); canos e fios de piscina, churrasqueira, jardim e lavabo
          num projeto só.
        </Nota>
        <OpPrograma titulo="A · Lavabo fechado (vaso + pia)" rec>
          <ProsContras
            tamanho={28}
            pros={<><li>Ninguém entra na casa molhado</li><li>Fica perto da piscina</li></>}
            contras={<><li>Precisa de esgoto novo</li><li>Pode não caber: depende da medida de quarta</li></>}
          />
        </OpPrograma>
        <OpPrograma titulo="B · Só uma pia de apoio na parede">
          <ProsContras
            tamanho={28}
            pros={<><li>Cabe em qualquer medida</li><li>Obra menor e mais barata</li></>}
            contras={<><li>Banheiro continua dentro da casa</li></>}
          />
        </OpPrograma>
        <Nota>O porcelanato 82×82 que você já comprou pode entrar aqui. Vamos ver juntos na quarta.</Nota>
      </Card>
    </div>
    <Rodape />
  </div>
);

// =====================================================================
// 9. MURO E PORTÃO
// =====================================================================
const Muro: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="O cartão de visita" titulo="Muro, portão e fachadas" />
    <Ambiente>
      <Foto src={fotoFachada} altura={500} tipo="hoje" legenda="Muro e portões atuais." />
      <Card estilo={{ padding: '20px 26px' }}>
        <div style={{ fontSize: 30, fontWeight: 700 }}>Como o portão abre</div>
        <Nota>
          Já certo: muro que impressiona (decisão 5) e fachadas lisas no mesmo estilo (decisão 4). No muro, só
          acabamento: a estrutura dele não muda.
        </Nota>
        <OpPrograma titulo="A · Portão de correr" rec>
          <ProsContras
            pros={<><li>Não ocupa a área de lazer ao abrir</li><li>Abre mostrando o projeto</li></>}
            contras={<><li>Precisa de trilho e espaço ao lado</li><li>Trilho junta sujeira</li></>}
          />
        </OpPrograma>
        <OpPrograma titulo="B · Portão de abrir (folhas)">
          <ProsContras
            pros={<><li>Sem trilho no chão</li><li>Instalação mais simples</li></>}
            contras={<><li>Folhas tomam a frente ao abrir</li><li>Vento bate a folha</li></>}
          />
        </OpPrograma>
      </Card>
      <Foto
        src={URL_MURO_VIDRO}
            contain
        altura={400}
        tipo="ref"
        legenda={
          <>
            <Parecido />: muro baixo de alvenaria com vidro em cima, na frente de uma casa. O vidro da foto é
            transparente; o proposto é espelhado. Foto: Rollit, via AECweb.
          </>
        }
      />
    </Ambiente>
    <Rodape />
  </div>
);

// =====================================================================
// 10a. LUZ — A PLANTA
// =====================================================================
const Ponto = ({ x, y, r, cor }: { x: number; y: number; r: number; cor: string }) => (
  <circle cx={x} cy={y} r={r} fill={cor} />
);

const Legenda = ({ cor, texto }: { cor: string; texto: string }) => (
  <div style={{ display: 'flex', alignItems: 'center', gap: 14, fontSize: 28 }}>
    <span style={{ width: 24, height: 24, borderRadius: '50%', background: cor, flex: 'none' }} />
    {texto}
  </div>
);

const LuzPlanta: Page = () => (
  <div style={pagina(true)}>
    <Cabecalho eyebrow="O ponto alto" titulo="Um botão para cada momento" />
    <p style={{ margin: 0, fontSize: 28, color: '#cfc8ba', lineHeight: 1.4 }}>
      As luzes da área de lazer são separadas em grupos. Cada momento acende só os grupos de que precisa. Você liga com{' '}
      <b style={{ color: CREME }}>um botão por momento</b> num teclado na parede (um perto da bancada, outro na saída da
      casa) <b style={{ color: CREME }}>ou pelo celular</b>.
    </p>
    <div style={{ display: 'grid', gridTemplateColumns: '760px 1fr', gap: 56, alignItems: 'start' }}>
      <div style={{ background: ESCURO_2, borderRadius: 'var(--osd-radius)', padding: 18 }}>
        <svg viewBox="0 0 300 260" width={724} height={560} role="img" aria-label="Planta simples com os pontos de luz">
          {/* Casa no centro; também ocupa o fundo do Corredor 1 e metade do L do Corredor 2. */}
          <rect x="10" y="10" width="280" height="225" fill="none" stroke="#8a8a80" strokeWidth="2" />
          <polygon points="10,12 150,12 150,36 240,36 240,130 60,130 60,80 10,80" fill="#3a4540" stroke="#8a8a80" />
          <text x="150" y="88" fill="#cfc8ba" fontSize="11" textAnchor="middle">CASA</text>
          <text x="35" y="104" fill="#cfc8ba" fontSize="8" textAnchor="middle">Corredor 1</text>
          <text x="35" y="116" fill="#cfc8ba" fontSize="8" textAnchor="middle">(lavabo)</text>
          <text x="260" y="78" fill="#cfc8ba" fontSize="8" textAnchor="middle">Corredor 2</text>
          <text x="260" y="90" fill="#cfc8ba" fontSize="8" textAnchor="middle">(jardim)</text>
          {/* Jardim rente ao muro: lateral direita e metade do fundo, até o fim do L */}
          <rect x="282" y="12" width="6" height="128" fill="#4f7a4f" />
          <rect x="190" y="12" width="98" height="6" fill="#4f7a4f" />
          <rect x="152" y="16" width="34" height="16" fill="none" stroke="#cfc8ba" strokeDasharray="3 2" />
          <text x="169" y="27" fill="#cfc8ba" fontSize="7" textAnchor="middle">escada</text>
          <text x="232" y="30" fill="#cfc8ba" fontSize="7" textAnchor="middle">fim do L</text>
          {/* Garagem = área de lazer nas reuniões (o carro sai); bancada paralela ao muro */}
          <rect x="168" y="146" width="98" height="78" rx="4" fill="none" stroke="#cfc8ba" strokeDasharray="4 3" />
          <text x="214" y="160" fill="#cfc8ba" fontSize="8" textAnchor="middle">garagem</text>
          <text x="214" y="170" fill="#cfc8ba" fontSize="7" textAnchor="middle">nas reuniões: mesas</text>
          <rect x="274" y="148" width="12" height="58" fill="#8a7a62" />
          <rect x="254" y="148" width="10" height="58" fill="#8a7a62" opacity="0.55" strokeDasharray="2 2" stroke="#cfc8ba" />
          <text x="210" y="204" fill="#cfc8ba" fontSize="7" textAnchor="middle">bancada paralela</text><text x="210" y="213" fill="#cfc8ba" fontSize="7" textAnchor="middle">ao muro (A ou B)</text>
          <rect x="30" y="148" width="120" height="55" rx="6" fill="#2a5a74" />
          <text x="90" y="179" fill="#e8f2f7" fontSize="10" textAnchor="middle">piscina</text>
          <line x1="10" y1="235" x2="290" y2="235" stroke="#cfc8ba" strokeWidth="4" />
          <rect x="190" y="231" width="60" height="8" fill={ESCURO} stroke="#cfc8ba" />
          <text x="150" y="254" fill="#cfc8ba" fontSize="9" textAnchor="middle">muro e portão (entrada do carro) · rua</text>
          <Ponto x={280} y={158} r={5} cor="#ffffff" />
          <Ponto x={280} y={177} r={5} cor="#ffffff" />
          <Ponto x={280} y={196} r={5} cor="#ffffff" />
          <Ponto x={190} y={188} r={4} cor="#f2b84b" />
          <Ponto x={238} y={188} r={4} cor="#f2b84b" />
          <Ponto x={45} y={175} r={4} cor="#5fd0ff" />
          <Ponto x={135} y={175} r={4} cor="#5fd0ff" />
          <Ponto x={270} y={45} r={3} cor="#9bd27a" />
          <Ponto x={270} y={110} r={3} cor="#9bd27a" />
          <Ponto x={270} y={132} r={3} cor="#9bd27a" />
          <Ponto x={205} y={26} r={3} cor="#9bd27a" />
          <Ponto x={258} y={26} r={3} cor="#9bd27a" />
          <Ponto x={35} y={92} r={3} cor="#9bd27a" />
          <Ponto x={243} y={60} r={3} cor="#f2b84b" />
          <Ponto x={243} y={110} r={3} cor="#f2b84b" />
          <Ponto x={60} y={228} r={3} cor="#e46a6a" />
          <Ponto x={130} y={228} r={3} cor="#e46a6a" />
          <Ponto x={180} y={228} r={3} cor="#e46a6a" />
          <Ponto x={260} y={228} r={3} cor="#e46a6a" />
        </svg>
        <p style={{ margin: '6px 0 0', fontSize: 22, color: '#cfc8ba' }}>
          Desenho simples, sem escala. Posições a confirmar na medição de 14/10.
        </p>
      </div>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 26, paddingTop: 20 }}>
        <div style={{ fontSize: 30, fontWeight: 700 }}>Cada cor é um grupo de luz</div>
        <Legenda cor="#ffffff" texto="Luz forte da bancada" />
        <Legenda cor="#f2b84b" texto="Luz amarela suave (mesas e parede)" />
        <Legenda cor="#5fd0ff" texto="Luz na água" />
        <Legenda cor="#9bd27a" texto="Luz baixa de caminho" />
        <Legenda cor="#e46a6a" texto="Muro e número da casa" />
        <p style={{ margin: '12px 0 0', fontSize: 28, color: '#cfc8ba' }}>
          Na próxima página: o que cada botão acende.
        </p>
      </div>
    </div>
    <Rodape escuro />
  </div>
);
LuzPlanta.transition = settle;

// =====================================================================
// 10b. LUZ — AS 4 CENAS
// =====================================================================
const Cena = ({
  nome,
  cor,
  acende,
  paraQue,
  comoLiga,
}: {
  nome: string;
  cor: string;
  acende: string;
  paraQue: string;
  comoLiga: string;
}) => (
  <div style={{ background: cor, borderRadius: 'var(--osd-radius)', padding: '20px 26px', marginBottom: 24, fontSize: 24, lineHeight: 1.35, color: '#eee' }}>
    <b style={{ display: 'block', fontSize: 34, fontFamily: 'var(--osd-font-display)', marginBottom: 6 }}>{nome}</b>
    {acende}
    <br />
    <span style={{ color: '#f0d9a8', fontWeight: 600 }}>Para quê:</span> {paraQue}
    <br />
    <span style={{ color: '#f0d9a8', fontWeight: 600 }}>Como liga:</span> {comoLiga}
  </div>
);

const LuzCenas: Page = () => (
  <div style={pagina(true)}>
    <Cabecalho eyebrow="O ponto alto" titulo="Quatro botões, quatro momentos" />
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 32, alignItems: 'start' }}>
      <div>
        <Steps>
          <Step>
            <Cena
              nome="Chegada"
              cor="#2d3a33"
              acende="Acendem as luzes do muro e o número da casa, e as luzes baixas do caminho do portão até a porta. O resto fica apagado."
              paraQue="chegar à noite vendo onde pisa e com a casa bonita para quem olha da rua."
              comoLiga='botão "Chegada" ou celular; pode acender sozinha quando escurece.'
            />
          </Step>
          <Step>
            <Cena
              nome="Churrasco"
              cor="#3b3022"
              acende="Luz forte e branca em cima da bancada, para enxergar a carne e cortar com segurança. Luz amarela suave sobre as mesas. Jardim fraco, só marcando o caminho."
              paraQue="cozinhar bem e conversar à mesa sem luz no olho."
              comoLiga='botão "Churrasco", no teclado ao lado da bancada.'
            />
          </Step>
        </Steps>
      </div>
      <div>
        <Steps>
          <Step>
            <Cena
              nome="Piscina"
              cor="#1f3340"
              acende="Só a luz dentro da água fica acesa, mais as luzes baixas em volta, para ninguém tropeçar. Bancada e mesas apagadas."
              paraQue="nadar à noite e ver a água brilhar."
              comoLiga='botão "Piscina". A luz da água vem com a piscina: combinamos com a loja.'
            />
          </Step>
          <Step>
            <Cena
              nome="Festa"
              cor="#33283a"
              acende="Tudo aceso, na medida certa: bancada, mesas, água, jardim do Corredor 2, luzes na parede da casa e o muro."
              paraQue="receber muita gente com a área toda viva."
              comoLiga='botão "Festa". Um outro botão apaga tudo de uma vez.'
            />
          </Step>
        </Steps>
      </div>
    </div>
    <Rodape escuro />
  </div>
);

// =====================================================================
// 11. COMO LER AS ESCOLHAS
// =====================================================================
const ComoLer: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="As suas escolhas" titulo="8 decisões de material, 2 caminhos em cada uma" />
    <div style={{ display: 'grid', gridTemplateColumns: '1.3fr 1fr', gap: 36, alignItems: 'start' }}>
      <Card>
        <div style={{ fontSize: 32, fontWeight: 700, marginBottom: 14 }}>Como ler as próximas páginas</div>
        <ul style={{ margin: 0, paddingLeft: 30, fontSize: 26, lineHeight: 1.4, display: 'flex', flexDirection: 'column', gap: 12 }}>
          <li>Cada página mostra <b>duas opções</b>, com o que é bom e o que é ruim em cada uma.</li>
          <li>A moldura verde e o selo <b>"a equipe recomenda"</b> mostram a nossa sugestão, com o porquê. <b>A escolha é sua.</b></li>
          <li>Comparamos sempre por 5 coisas: <b>preço, limpeza, durar muito, calor no sol e estilo simples</b>.</li>
          <li><Mesmo />: é a foto do produto que vamos usar. <Parecido />: é só para você ter ideia.</li>
          <li>Todas as fotos são de casas, no mesmo uso que o seu.</li>
        </ul>
      </Card>
      <Card>
        <div style={{ fontSize: 32, fontWeight: 700, marginBottom: 14 }}>O que já ficou de fora</div>
        <ul style={{ margin: 0, paddingLeft: 30, fontSize: 26, lineHeight: 1.4, display: 'flex', flexDirection: 'column', gap: 12 }}>
          <li><b>Policarbonato</b>: amarela, suja e dá trabalho.</li>
          <li><b>Cerâmica na fachada inteira</b>: cara e demorada.</li>
          <li><b>Nichos e prateleiras abertas</b>: juntam poeira.</li>
        </ul>
        <Nota>
          Os preços de cada opção chegam com o orçamento da obra. Por enquanto, "mais caro" e "mais barato" é comparação
          entre as duas, sem número.
        </Nota>
      </Card>
    </div>
    <Rodape />
  </div>
);

// =====================================================================
// 12–19. AS 8 DECISÕES
// =====================================================================
const Decisao = ({
  eyebrow,
  titulo,
  a,
  b,
  porque,
}: {
  eyebrow: string;
  titulo: string;
  a: ReactNode;
  b: ReactNode;
  porque: ReactNode;
}) => (
  <div style={{ ...pagina(), gap: 22 }}>
    <Cabecalho eyebrow={eyebrow} titulo={titulo} />
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 32, alignItems: 'start' }}>
      {a}
      {b}
    </div>
    <Steps>
      <Step>
        <Recomenda>{porque}</Recomenda>
      </Step>
    </Steps>
    <Rodape />
  </div>
);

const ALT = 230;

const D1Piso: Page = () => (
  <Decisao
    eyebrow="Decisão 1 de 8 · Chão do jardim"
    titulo="Placas com grama no meio, ou piso inteiro?"
    a={
      <OpDecisao
        rec
        titulo="A · Placa de concreto + grama sintética"
        fotos={
          <DuasFotos>
            <Foto
              src="https://api.aecweb.com.br/cls/anuncios/pes_33379/pisadeira-de-concreto-ecoverde-med.webp"
              altura={ALT - 40}
              legenda={<><Mesmo />: Pisadeira de Concreto, Eco Verde. Fabricante via AECweb.</>}
            />
            <Foto
              src="https://www.playgrama.com.br/wp-content/uploads/2020/07/mosaicocapa20mmbicolor.jpg"
              altura={ALT - 40}
              legenda={<><Mesmo />: Grama Sintética 20 mm Bicolor, PlayGrama.</>}
            />
          </DuasFotos>
        }
      >
        <ProsContras
          pros={<><li>A chuva some pelas juntas: sem poça, sem limo</li><li>Sempre verde, sem cortar nem regar</li><li>Assenta na areia, sem contrapiso</li></>}
          contras={<><li>Grama sintética esquenta no sol forte</li><li>Folha e sujeira presas pedem vassoura</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Piso inteiro (porcelanato de área externa)"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1788398913509-89f16ab3ab9c?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: piso cerâmico inteiro em área externa. Foto: David Marquez / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Limpa com rodo e mangueira</li><li>Visual liso e contínuo</li><li>Pode usar o mesmo piso da casa</li></>}
          contras={<><li>Precisa de contrapiso, caimento e ralo</li><li>Rejunte escurece com o tempo</li><li>Pode escorregar molhado</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> você não quer limo nem trabalho. A água infiltra sozinha e não há grama de verdade para cuidar.</>}
  />
);

const D2Borda: Page = () => (
  <Decisao
    eyebrow="Decisão 2 de 8 · Borda da piscina"
    titulo="Borda que não esquenta, ou borda de cerâmica?"
    a={
      <OpDecisao
        rec
        titulo="A · Borda atérmica clara (Braston)"
        fotos={
          <Foto
            src={URL_BORDA}
            altura={ALT}
            tipo="ref"
            legenda={<><Mesmo />: Borda de Piscina Braston, textura atérmica fulgê. Fabricante via AECweb.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Não queima o pé no sol</li><li>Não escorrega</li><li>Branco, crema, areia ou cinza</li></>}
          contras={<><li>Clara, mostra sujeira e precisa de lavagem</li><li>Revenda no Rio ainda a confirmar</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Borda de cerâmica comum"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1759854909332-b73cdb19b705?fm=jpg&q=70&w=600"
            altura={ALT}
            tipo="ref"
            legenda={<><Parecido />: borda em lajota cerâmica. Foto: Joachim Lesne / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Fácil de achar em qualquer loja</li><li>Muitas cores e tamanhos</li></>}
          contras={<><li>Esquenta muito no sol do Rio</li><li>Rejunte junta limo perto da água</li><li>Pode escorregar molhada</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> em Irajá o sol é forte. Uma borda que queima o pé estraga o uso da piscina.</>}
  />
);

const D3Bancada: Page = () => (
  <Decisao
    eyebrow="Decisão 3 de 8 · Bancada do churrasco"
    titulo="Bancada escura, ou bancada clara?"
    a={
      <OpDecisao
        rec
        titulo="A · Granito Preto São Gabriel"
        fotos={
          <DuasFotos>
            <Foto
              src="https://api.aecweb.com.br/cls/anuncios/pes_124214/pq-preto-sao-gabriel.webp"
              altura={ALT - 40}
              tipo="prod"
              legenda="Granito Preto São Gabriel (chapa, Kadosh Stone). AECweb."
            />
            <Foto
              src="https://thumb-cdn.soluall.net/prod/shp_products/sp1024mw/611a7066-46cc-4341-a0fb-2e4fac1e09ff/611a7066-2488-4b7d-9982-2e4fac1e09ff.jpg"
              altura={ALT - 40}
              legenda={<><Mesmo /> (mesma pedra), em bancada de churrasqueira. Foto: R.R Marmoraria, via Solutudo.</>}
            />
          </DuasFotos>
        }
      >
        <ProsContras
          pros={<><li>Aguenta panela quente e carvão</li><li>Quase não mancha: gordura sai com pano</li><li>Comum nas marmorarias do Rio</li></>}
          contras={<><li>Escura, esquenta se pegar sol direto</li><li>Mostra marca de dedo e de água</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Bancada clara (pedra ou quartzo branco)"
        fotos={
          <Foto
            src={URL_BANCADA_REF}
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: bancada clara com churrasqueira, em casa (pedra exata não informada). Foto: Salvo Media LLC / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Visual leve e mais minimalista</li><li>Esquenta menos no sol</li></>}
          contras={<><li>Mancha com gordura, vinho e carvão</li><li>Quartzo pode marcar com panela quente</li><li>Pede mais cuidado na limpeza</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> numa bancada de churrasco, mancha é o maior problema. A pedra escura esconde e limpa fácil.</>}
  />
);

const D4Fachada: Page = () => (
  <Decisao
    eyebrow="Decisão 4 de 8 · Fachadas"
    titulo="Revestimento que já vem na cor, ou pintura?"
    a={
      <OpDecisao
        rec
        titulo="A · Revestimento mineral colorido (Minerale)"
        fotos={
          <DuasFotos>
            <Foto
              src="https://api.aecweb.com.br/cls/anuncios/pes_51191/minerale-quartzolit-atualiza%C3%A7ao.webp"
              altura={ALT - 40}
              contain
              tipo="prod"
              legenda="Minerale, Quartzolit. AECweb."
            />
            <Foto
              src="https://api.aecweb.com.br/matoutros/img_figuras/olho_340x216_Olho$$13301.webp"
              altura={ALT - 40}
              legenda={<><Mesmo />: Minerale branco na fachada de uma casa. Estudo de caso Quartzolit.</>}
            />
          </DuasFotos>
        }
      >
        <ProsContras
          pros={<><li>Já vem na cor: não precisa pintar</li><li>Dura mais que tinta na chuva e no sol</li><li>Pedreiro de reboco sabe aplicar</li></>}
          contras={<><li>Cores limitadas ao catálogo</li><li>Retoque pode ficar com tom diferente</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Massa lisa + tinta para área externa"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1787590006095-b33b262ef93c?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: fachada com reboco pintado de branco; repare como a pintura gasta. Foto: Javier Balseiro / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Qualquer cor que você quiser</li><li>Fácil de retocar e trocar de cor</li></>}
          contras={<><li>Precisa repintar de tempos em tempos</li><li>Suja e descasca mais fácil (como o Corredor 2 hoje)</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> você não quer manutenção. Hoje a parede descasca; o revestimento mineral evita repintar.</>}
  />
);

const D5Muro: Page = () => (
  <Decisao
    eyebrow="Decisão 5 de 8 · Muro da frente"
    titulo="Faixas de vidro espelhado, ou ripas verticais?"
    a={
      <OpDecisao
        rec
        titulo="A · Faixas de vidro espelhado laminado"
        fotos={
          <Foto
            src={URL_MURO_VIDRO}
            contain
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: muro baixo de casa com vidro em cima (na foto, transparente; o proposto é espelhado, Cebrace Reflecta). Foto: Rollit, via AECweb.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Quem passa vê o reflexo; você vê a rua</li><li>O efeito de impacto que você pediu</li><li>Laminado não estilhaça</li></>}
          contras={<><li>Mostra poeira e chuva: limpar com rodo</li><li>À noite, com luz dentro, fica transparente</li><li>Vidraçaria no Rio a confirmar</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Ripas verticais (metal com pintura de madeira)"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1691821331552-ab4f12500a24?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: muro de ripas na frente de uma casa (madeira de verdade; a nossa seria metal). Foto: Jacob Walsh / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Visual quente e de linhas retas</li><li>Não mostra poeira como o vidro</li></>}
          contras={<><li>Pintura precisa de retoque com o sol</li><li>Entre as ripas junta folha e poeira</li><li>Menos "uau" que o espelho</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> foi o seu pedido de muro que impressiona. O vidro se limpa com rodo, sem pintura.</>}
  />
);

const SemFoto = () => (
  <div
    style={{
      height: ALT + 20,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      textAlign: 'center',
      background: '#efebe3',
      borderRadius: 10,
      color: AVISO,
      fontSize: 26,
      fontWeight: 600,
      padding: 30,
      boxSizing: 'border-box',
    }}
  >
    Sem foto aplicada. Ainda não encontramos foto da telha trapezoidal sanduíche instalada. Mostraremos amostra ou obra
    real antes da escolha.
  </div>
);

const D6Cobertura: Page = () => (
  <Decisao
    eyebrow="Decisão 6 de 8 · Cobertura do churrasco"
    titulo="Telha que não esquenta: colonial, ou reta?"
    a={
      <OpDecisao
        titulo="A · Telha sanduíche colonial (Isotelha)"
        fotos={
          <DuasFotos>
            <Foto
              src="https://api.aecweb.com.br/cls/anuncios/pes_18190/1_260x240.webp"
              altura={ALT - 40}
              contain
              tipo="prod"
              legenda="Isotelha Colonial, Kingspan Isoeste (corte com isolante). AECweb."
            />
            <Foto
              src="https://api.aecweb.com.br/matoutros/img_figuras/olho_245x260_Olho$$6449.webp"
              altura={ALT - 40}
              legenda={<><Mesmo />: Isotelha Colonial instalada. Matéria Kingspan Isoeste.</>}
            />
          </DuasFotos>
        }
      >
        <ProsContras
          pros={<><li>Isolante no meio: menos calor e barulho de chuva</li><li>Parece telha de barro, mas é leve</li></>}
          contras={<><li>Ondulada: foge das linhas retas</li><li>Ondas juntam folha e sujeira</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao rec titulo="B · Telha sanduíche trapezoidal (reta)" fotos={<SemFoto />}>
        <ProsContras
          pros={<><li>Mesmo isolante: menos calor e barulho</li><li>Linhas retas, estilo simples</li><li>Por baixo, forro liso e fácil de limpar</li></>}
          contras={<><li>Visual "de galpão" se ficar à mostra</li><li>Ainda sem foto do produto instalado</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda B:</b> as duas isolam igual; a reta conversa com o seu gosto por linhas retas. Antes de decidir, mostramos uma foto real dela instalada.</>}
  />
);

const D7Escada: Page = () => (
  <Decisao
    eyebrow="Decisão 7 de 8 · Escada nova"
    titulo="Escada de alvenaria, ou de metal?"
    a={
      <OpDecisao
        rec
        titulo="A · Concreto ou alvenaria, degrau largo"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1768941124452-9a624bb5c8ab?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: escada reta de alvenaria, do lado de fora, colada na parede de uma casa. Foto: Kellen Riggin / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Não enferruja, quase sem manutenção</li><li>Firme, não balança nem faz barulho</li><li>Pode receber o piso da casa</li></>}
          contras={<><li>Obra mais demorada (forma e cura)</li><li>Pesada: precisa de base calculada</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Metal (chapa dobrada)"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1760896743899-8e20e3fa2b7a?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: escadas de metal do lado de fora de casas (em caracol; a sua seria reta). Foto: Y.A / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Leve e rápida de montar</li><li>Visual fino e moderno</li></>}
          contras={<><li>Ao tempo: pode enferrujar, pede pintura</li><li>Faz barulho ao pisar</li><li>Esquenta no sol</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> fica ao tempo e você não quer manutenção. Se for construir em cima, a escolha final depende desse projeto.</>}
  />
);

const D8Luz: Page = () => (
  <Decisao
    eyebrow="Decisão 8 de 8 · Como ligar a luz"
    titulo="Botão por momento ou interruptor comum?"
    a={
      <OpDecisao
        rec
        titulo="A · Um botão (ou o celular) para cada momento"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1788619371179-b3031f2cbe23?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: jardim com luz por grupos. Foto: Val Vesa / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Um toque por momento (Chegada, Festa…)</li><li>Liga pelo celular</li><li>Dá para ampliar à casa</li></>}
          contras={<><li>Mais caro que interruptor comum</li><li>Precisa de Wi-Fi bom</li></>}
        />
      </OpDecisao>
    }
    b={
      <OpDecisao
        titulo="B · Interruptores comuns, um por grupo"
        fotos={
          <Foto
            src="https://images.unsplash.com/photo-1556217994-22de7face210?fm=jpg&q=70&w=600"
            altura={ALT - 40}
            tipo="ref"
            legenda={<><Parecido />: interruptor simples na parede. Foto: Isabella Fischer / Unsplash.</>}
          />
        }
      >
        <ProsContras
          pros={<><li>Mais barato e simples</li><li>Qualquer eletricista conserta</li></>}
          contras={<><li>Para "Festa", liga um por um</li><li>Mais teclas na parede</li><li>Sem controle pelo celular</li></>}
        />
      </OpDecisao>
    }
    porque={<><b>Por que a equipe recomenda A:</b> é o ponto alto, e os fios já vão ser refeitos agora: sai mais barato que mexer depois.</>}
  />
);

// =====================================================================
// 20. CUSTO
// =====================================================================
const Custo: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Quanto custa" titulo="Projeto e obra, separados" />
    <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: 36, alignItems: 'start' }}>
      <Card>
        <div style={{ display: 'flex', alignItems: 'baseline', gap: 28 }}>
          <div style={{ fontSize: 32, fontWeight: 700 }}>Projeto da sua reforma</div>
          <div style={{ fontFamily: 'var(--osd-font-display)', fontSize: 88, color: VERDE, fontWeight: 600, lineHeight: 1 }}>
            R$ 3.500
          </div>
        </div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 28, marginTop: 18 }}>
          <ul style={{ margin: 0, paddingLeft: 26, fontSize: 24, lineHeight: 1.35 }}>
            <li>Medição da casa e estudo com 3 perspectivas</li>
            <li>Os 4 ambientes projetados, com iluminação em cenas</li>
            <li>Elétrica e hidráulica das áreas externas</li>
            <li>Marcenaria da área gourmet</li>
            <li>Lista de quantidades para a obra</li>
            <li>Reunião com o fornecedor da piscina</li>
            <li>Apresentação final</li>
          </ul>
          <ul style={{ margin: 0, paddingLeft: 26, fontSize: 26, lineHeight: 1.35, display: 'flex', flexDirection: 'column', gap: 10 }}>
            <li><b>Revisões sem limite.</b> Ajustamos até ficar do seu jeito.</li>
            <li><b>2º pavimento de presente</b>, por fazer a obra com a Sttickler.</li>
            <li>
              <b>Esse valor volta para você na obra.</b> Se contratar a obra com a Sttickler, os R$ 3.500 são descontados
              do preço da obra. Se não fizer a obra conosco, o projeto é seu do mesmo jeito.
            </li>
          </ul>
        </div>
        <p style={{ margin: '16px 0 0', fontSize: 20, color: MUTED, lineHeight: 1.35 }}>
          Fonte: Severiano (orçamentista Sttickler), Orçamento do Projeto Adriana v3, 11/10/2026. Não inclui:
          acompanhamento de obra; projeto estrutural (pergolado, escada, base da piscina); projeto da piscina (da loja);
          aprovação em prefeitura ou condomínio; ART/RRT e honorários de terceiros; impressão.
        </p>
      </Card>
      <Card>
        <div style={{ fontSize: 32, fontWeight: 700, marginBottom: 16 }}>Obra</div>
        <span
          style={{
            display: 'inline-block',
            background: '#fff4dc',
            color: AVISO,
            borderRadius: 8,
            padding: '8px 16px',
            fontSize: 28,
            fontWeight: 700,
          }}
        >
          Aguardando orçamento
        </span>
        <p style={{ margin: '20px 0 0', fontSize: 28, color: MUTED, lineHeight: 1.4 }}>
          Vamos mostrar uma faixa (mínimo e máximo) e o que não está incluído, já com as opções que você escolher aqui.
          Nenhum número aparece antes do orçamento pronto.
        </p>
      </Card>
    </div>
    <Rodape />
  </div>
);

// =====================================================================
// 21. PRÓXIMOS PASSOS
// =====================================================================
const Passo = ({ titulo, texto }: { titulo: string; texto: string }) => (
  <div style={{ display: 'grid', gridTemplateColumns: '420px 1fr', gap: 32, borderTop: `1px solid ${LINE}`, padding: '22px 0' }}>
    <div style={{ fontFamily: 'var(--osd-font-display)', fontSize: 40, fontWeight: 600 }}>{titulo}</div>
    <div style={{ fontSize: 30, color: MUTED, lineHeight: 1.4 }}>{texto}</div>
  </div>
);

const Proximos: Page = () => (
  <div style={pagina()}>
    <Cabecalho eyebrow="Próximos passos" titulo="Como vamos caminhar juntos" />
    <div>
      <Steps>
        <Step>
          <Passo
            titulo="1 · Quarta, 14/10, 16h"
            texto="Medir tudo: a frente do Corredor 2 para a bancada, o Corredor 1 para o lavabo e o fundo para a escada. Falar da piscina e do andar de cima."
          />
        </Step>
        <Step>
          <Passo
            titulo="2 · Suas escolhas"
            texto="Você escolhe o que entra em cada espaço e uma opção em cada uma das 8 decisões. Pode mudar depois: revisões sem limite."
          />
        </Step>
        <Step>
          <Passo
            titulo="3 · Projeto"
            texto="Desenho, imagens do depois e o projeto único de canos e fios. Orçamento da obra com as suas escolhas."
          />
        </Step>
        <Step>
          <Passo titulo="4 · Obra" texto="Previsão: janeiro de 2027." />
        </Step>
      </Steps>
    </div>
    <Rodape />
  </div>
);

// =====================================================================
// 22. CHECAGEM
// =====================================================================
const Pergunta = ({ children }: { children: ReactNode }) => (
  <div style={{ fontSize: 32, lineHeight: 1.35, padding: '14px 0 14px 26px', borderLeft: '4px solid #d9895a', marginBottom: 18 }}>
    {children}
  </div>
);

const Checagem: Page = () => (
  <div style={pagina(true)}>
    <Cabecalho eyebrow="Antes de seguir" titulo="Me conta com as suas palavras" />
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 56, alignItems: 'start' }}>
      <div>
        <Steps>
          <Step><Pergunta>Onde vai ficar o churrasco, e onde ficam as mesas?</Pergunta></Step>
          <Step><Pergunta>O que mais você quer na piscina, e onde?</Pergunta></Step>
          <Step><Pergunta>Das 8 decisões, qual você já sabe e qual quer pensar mais?</Pergunta></Step>
        </Steps>
      </div>
      <div>
        <Steps>
          <Step><Pergunta>O que acontece com o valor do projeto se você fizer a obra com a gente?</Pergunta></Step>
          <Step><Pergunta>Qual botão de luz você usaria numa festa, e o que ele acende?</Pergunta></Step>
          <Step><Pergunta>O que ainda ficou sem resposta para você?</Pergunta></Step>
        </Steps>
      </div>
    </div>
    <p style={{ margin: 0, fontSize: 30, color: '#cfc8ba' }}>
      Não existe pergunta boba. Se algo não ficou claro, a culpa é nossa, e explicamos de novo.
    </p>
    <Rodape escuro />
  </div>
);
Checagem.transition = settle;

// =====================================================================
export const meta: SlideMeta = {
  title: 'Adriana (Irajá) · Proposta visual',
  createdAt: '2026-10-11T12:00:00Z',
};

export default [
  Capa,
  Pedido1,
  Pedido2,
  Hoje,
  Piscina,
  Gourmet,
  Mesas,
  Jardim,
  Escada,
  Lavabo,
  Muro,
  LuzPlanta,
  LuzCenas,
  ComoLer,
  D1Piso,
  D2Borda,
  D3Bancada,
  D4Fachada,
  D5Muro,
  D6Cobertura,
  D7Escada,
  D8Luz,
  Custo,
  Proximos,
  Checagem,
] satisfies Page[];

export const notes: (string | undefined)[] = [
  // 1 Capa
  `Abra agradecendo a casa e o tempo dela. Diga que isto é uma proposta, não um projeto pronto: ela escolhe.
Pergunte: "Você já mostrou estas fotos para alguém da família? O que eles acharam da ideia?"`,
  // 2 Pedido 1
  `Leia os três espaços como quem confere a lista do mercado: "foi isso que eu ouvi, certo?".
Pergunte: "Faltou alguma coisa na piscina, no gourmet ou no jardim? Algo aqui você não quer?"`,
  // 3 Pedido 2
  `Lavabo, muro e escada. Lembre que o lavabo depende da medição de quarta.
Feche com a frase da regra: bonita, barata de fazer e fácil de limpar.
Pergunte: "Essa regra vale para você? Tem algo em que você aceitaria gastar mais?"`,
  // 4 Hoje
  `Mostre as quatro fotos e nomeie os lugares: brita = piscina, Corredor 2 = jardim, Corredor 1 = lavabo.
Pergunte: "Combinado chamar de Corredor 1 e Corredor 2 daqui para frente?"`,
  // 5 Piscina
  `Já certo: piscina na brita, piso quase no nível da calçada, fios por baixo do chão a partir do poste dela.
Destaque: a equipe recomenda a prainha. A loja da piscina responde pela piscina.
Pergunte: "Prainha ou cascata? Você já sabe o modelo da piscina que vai ganhar?"`,
  // 6 Gourmet bancada
  `Aponte na foto: a bancada fica na frente da entrada do Corredor 2, não dentro dele.
Recomendação: bancada A (com cooktop e chapa).
Pergunte: "Quantas pessoas costumam vir num churrasco? Você usaria a chapa no dia a dia?"`,
  // 7 Mesas
  `Decisão rápida. Fixa é firme e limpa com mangueira; soltas liberam espaço mas precisam ser guardadas.
Pergunte: "Você imagina a frente vazia em algum dia, para festa ou carro?"`,
  // 8 Jardim
  `O jardim vai do começo ao fim do Corredor 2, rente ao muro. A referência é só para ideia, não é projeto nosso.
Recomendação: pergolado aberto.
Pergunte: "Você usaria o jardim na chuva? Se sim, o vidro faz sentido."`,
  // 9 Escada
  `A caracol sai. A nova fica no fundo, no ponto da foto.
Recomendação: reta, colada na parede da casa.
Pergunte: "Você pensa em construir em cima? Se sim, desenhamos junto, sem custo a mais no projeto."`,
  // 10 Lavabo
  `Mostre o limo: o piso com caimento e ralo acaba com ele.
Recomendação: lavabo fechado, se couber. Só a medição de quarta diz.
Pergunte: "Se não couber o vaso, a pia de apoio já resolve para você?" Lembre do porcelanato 82×82 que ela comprou.`,
  // 11 Muro
  `O muro só ganha acabamento; a estrutura não muda. A foto da direita é uma obra de arte, só para mostrar o efeito do espelho.
Recomendação: portão de correr.
Pergunte: "Quando o portão abre, o que você quer que a rua veja primeiro?"`,
  // 12 Luz planta
  `Este é o ponto alto. Explique devagar: cada cor da planta é um grupo de luz.
Mostre onde fica cada teclado: um perto da bancada, outro na saída da casa. E o celular.
Pergunte: "Dá para entender o que cada cor acende?"`,
  // 13 Luz cenas
  `Avance uma cena por vez e conte como uma história: chegar em casa, fazer o churrasco, nadar à noite, receber a festa.
Pergunte: "Qual desses momentos você mais vai usar? Falta algum momento seu?"`,
  // 14 Como ler
  `Explique a leitura antes das 8 decisões: duas opções, moldura verde é a nossa sugestão, a escolha é dela.
Verde "mesmo produto" é o que vamos usar; amarelo "material parecido" é só ideia.
Diga que preço de cada opção chega com o orçamento da obra.`,
  // 15 D1
  `Chão do jardim. Recomendamos placa + grama sintética: chuva some pelas juntas, sem limo.
Pergunte: "O calor da grama sintética no sol te incomoda?"`,
  // 16 D2
  `Borda da piscina. Recomendamos a atérmica: não queima o pé. A revenda no Rio ainda vamos confirmar.
Pergunte: "Qual cor você prefere: branco, crema, areia ou cinza?"`,
  // 17 D3
  `Bancada. Recomendamos o Preto São Gabriel: esconde mancha de churrasco.
Pergunte: "Você prefere praticidade ou o visual claro, mesmo com mais cuidado?"`,
  // 18 D4
  `Fachadas. Recomendamos o Minerale: já vem na cor e não precisa repintar.
Pergunte: "Tem alguma cor que você já imagina na fachada?"`,
  // 19 D5
  `Muro. Seja honesto: a foto mostra o muro certo, mas com vidro transparente; não achamos foto de muro de casa com vidro espelhado. O produto a cotar é o Cebrace Reflecta.
Avise: à noite, com luz dentro, o espelho fica transparente.
Pergunte: "Isso te incomoda, ou as ripas te agradam mais?"`,
  // 20 D6
  `Cobertura. Recomendamos a trapezoidal, mas ainda não temos foto dela instalada: prometa mostrar amostra ou obra real antes da escolha.
Pergunte: "Você gosta do ar de telha de barro, ou prefere tudo reto?"`,
  // 21 D7
  `Escada. Recomendamos alvenaria: não enferruja. A foto do metal é de caracol; a dela seria reta.
Pergunte de novo sobre construir em cima, porque muda a escolha.`,
  // 22 D8
  `Volta ao ponto alto. Os fios já vão ser refeitos, então deixar pronto agora custa menos que mexer depois.
Pergunte: "Você usa bem o celular para esse tipo de coisa? O Wi-Fi chega bem na frente da casa?"`,
  // 23 Custo
  `Fale o valor com calma: projeto R$ 3.500, fonte Severiano, orçamento v3.
O ponto principal: se ela fizer a obra com a Sttickler, esse valor é descontado da obra. Se não fizer, o projeto é dela.
A obra ainda está aguardando orçamento; não arrisque número.
Pergunte: "Ficou claro o que está incluído e o que não está?"`,
  // 24 Próximos
  `Avance passo a passo. Confirme a visita de quarta, 14/10, às 16h.
Pergunte: "Quarta às 16h continua bom para você? Quem mais vai estar em casa?"`,
  // 25 Checagem
  `Não leia as perguntas como prova. Faça uma de cada vez e deixe ela responder com as palavras dela.
Se alguma resposta sair diferente do que mostramos, volte à página e explique de novo.`,
];

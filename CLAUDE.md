# Gerando Tráfego: landing page

Contexto para o Claude Code. Projeto iniciado numa conversa no claude.ai em 31/10/2026.

## O que é
Landing page de captação para o **Gerando Tráfego**, serviço de gestão de tráfego pago (Meta Ads e Google Ads).
Objetivo da página: gerar leads qualificados no WhatsApp via "diagnóstico/análise gratuita".
Dono: Wesley Sá (Dáblio Comunicação, Mossoró/RN).

Bio da marca usada como base da copy:
- Melhor gestor de tráfego 2022
- Alavancando seu faturamento
- Em busca do seu melhor cliente

## Estrutura dos arquivos
- `index.html`: o site final. Arquivo único, autocontido (CSS, JS, logo e ícones em SVG inline). É o que vai para a hospedagem.
- `src/template.html`: fonte editável. Contém os marcadores `{{LOGO}}`, `{{SYMBOL}}`, `{{MARQUEE}}`, `{{CURSOR}}` e `{{CURSOR_HOVER}}`.
- `build.py`: gera o `index.html` a partir do template e dos SVGs (`python3 build.py`). Também falha se houver travessão (em dash) no texto.
- `src/logos/`: logos originais da marca em SVG.

Fluxo de edição: alterar `src/template.html`, rodar `python3 build.py`, conferir o `index.html`.

## Identidade visual
- Verde da marca: `#3dcb7f`. Acento lima: `#b8f55a`. Gradiente dos botões: lima para verde.
- Fundo escuro `#050806`, cards `#0b120e`. As seções intercalam fundo escuro e claro: classe `.light` na `<section>` troca as variáveis de cor; classe `.dark` cria um bloco escuro dentro de seção clara (foto do "quem sou" e caixa do CTA final).
- Hovers em botões, chips, cards, lista e FAQ, mais um brilho que segue o mouse nos cards (`.spot`, criado via JS). Só em aparelhos com mouse (`@media (hover:hover)`).
- Cursor do mouse vira o foguete da marca (`src/logos/foguete.svg`) só nas áreas pretas; nas seções claras volta o cursor normal. Em links e botões o foguete fica lima. O `build.py` gera o cursor (marcadores `{{CURSOR}}` e `{{CURSOR_HOVER}}`).
- Fonte: Manrope (Google Fonts), pesos 300 a 800.
- Visual inspirado num template Elementor (página de curso de importação) que foi reconstruído em código limpo: cards com glow, faixa rolante, jornada em 3 passos, card de oferta, selo, "quem sou" e FAQ.

## Seções (em ordem)
1. Hero: selo "Eleito melhor gestor de tráfego de 2022", título "Anúncio que vira faturamento, não só curtida", chips com as duas frases da bio, CTA, visual com símbolo e cards de métricas animados (sem números inventados).
2. Faixa rolante (Meta Ads, Google Ads, etc.).
3. Dores (4 cards).
4. Serviços (4 cards): estratégia, campanhas Meta e Google, rastreamento, otimização.
5. Jornada em 3 passos: diagnóstico, plano e implementação, otimização e escala.
6. Métricas CPL, CPA, ROAS, conversão + comparativo "só impulsionar" x "gestão estratégica".
7. Pra quem é (qualificação do cliente).
8. Diagnóstico gratuito (`#diagnostico`): formulário (nome, segmento, faturamento, investimento atual) que monta a mensagem do WhatsApp + selo "R$ 0 / risco zero".
9. Quem está por trás (foto ainda é placeholder com o símbolo).
10. FAQ (6 perguntas).
11. CTA final e rodapé. Botão flutuante de WhatsApp.

## WhatsApp
- Número: `5584994484226` (constante `WHATSAPP_NUMBER` no fim do arquivo).
- Mensagem base: "Olá! Vim pelo site Gerando Tráfego e gostaria de solicitar minha avaliação gratuita". O formulário acrescenta os campos preenchidos.

## Pendências
- Foto e nome do gestor na seção "Quem está por trás" (trocar o bloco `.ph` por `<img>`).
- Confirmar o nome da premiação de 2022 e se o serviço inclui relatórios (citado no FAQ).
- Seção de resultados/depoimentos: só com prints e depoimentos reais, nunca inventados.

## Hospedagem
- No ar em https://gerandotrafego.dablioagencia.com (Hostinger, conta u869810459, pasta `public_html/gerandotrafego`).
- Deploy automático: a Hostinger está ligada a este repositório (branch `main`). Todo push publica o site.
- O repositório inteiro é copiado para a hospedagem; o `.htaccess` bloqueia o acesso público a `.md`, `.py`, `src/` e `.git`. Arquivo novo que não deva ser público precisa entrar nessa regra.
- Prévia antiga também publicada como artifact no claude.ai.

## Regras de copy e comunicação (preferências do Wesley)
- Nunca usar travessão (em dash) nem emojis.
- Siglas (CPA, ROAS, CPL...) com o significado por extenso na primeira menção.
- Respostas diretas, organizadas e objetivas, sem perder a criatividade.
- Não inventar números, depoimentos ou resultados.

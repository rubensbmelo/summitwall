# Summit Wall Solutions — Roadmap (continuar amanhã)

Status: site multi-página rodando local. Menu corrigido. Favicon pronto. Logo do header ajustada (58px, à esquerda).
Próximo: subir pro GitHub (rubensbmelo/summitwall) e atacar SEO + conversão.

REGRA: deploy e git push SEMPRE feitos pelo Rubens (não pelo Claude Code).

====================================================================
ORDEM DE EXECUÇÃO (juntando nossa pesquisa + análise SEO recebida)
====================================================================

## 1. FORMULÁRIO REAL (Web3Forms) — PRIORIDADE MÁXIMA (converte)
Hoje FORM_ACCESS_KEY='' no js/main.js → cai no mailto (ruim).
Tarefa Claude Code:
  "Wire the contact form to Web3Forms. I'll paste the access key into
   FORM_ACCESS_KEY in js/main.js. Make sure success/error states work and
   it still falls back to mailto if the request fails."
AÇÃO RUBENS: criar conta grátis em https://web3forms.com, pegar a access key.

## 2. SCHEMA LocalBusiness + FAQPage (JSON-LD) — SEO alto valor
Não existe schema hoje. Adicionar via build.py em todas as páginas:
  - HomeAndConstructionBusiness / LocalBusiness (nome, telefone 587-357-8181,
    email, endereço Edmonton AB, areaServed: Edmonton + cidades, openingHours
    Mon-Fri 7-17, priceRange, sameAs Instagram)
  - Service schema nas páginas de serviço
  - FAQPage schema onde há FAQ
  - BreadcrumbList
Tarefa Claude Code:
  "Add JSON-LD structured data in build.py: a LocalBusiness/HomeAndConstructionBusiness
   block on every page (name, phone 587-357-8181, email, Edmonton AB, areaServed list,
   openingHours Mo-Fr 07:00-17:00, sameAs Instagram), FAQPage schema on pages with FAQ,
   and BreadcrumbList. Inject into <head>. Rebuild."

## 3. TÍTULOS focados em "Drywall Contractor" — SEO
Trocar títulos. Ex:
  Home:  "Drywall Contractor in Edmonton, AB | Summit Wall Solutions"
  Cidade:"Drywall Contractor in Sherwood Park, AB | Framing, Taping & Painting"
O termo "Drywall Contractor" precisa aparecer forte (title, H1, primeiro parágrafo).
Tarefa Claude Code:
  "Rewrite page <title> tags and hero copy to lead with 'Drywall Contractor in
   <City>, AB'. Update build.py and pages/bodies.py. Keep brand name after the pipe."

## 4. AJUSTES TÉCNICOS rápidos
  - Canonical da home: usar https://summitwallsolutions.ca/  (não /index.html)
  - Adicionar og:image (usar logo-lockup ou uma foto de obra) + twitter:card
  - Criar página 404.html
  - Criar privacy.html (política de privacidade — necessária pois capta formulário)
Tarefa Claude Code:
  "Fix home canonical to the bare domain. Add og:image and twitter:card meta to head().
   Create a 404.html and a privacy.html using the same header/footer template. Rebuild."

## 5. CONTEÚDO ÚNICO por cidade — SEO (evitar 'conteúdo fraco/duplicado')
Cada página de cidade precisa de texto próprio:
  - bairros atendidos
  - tipo de obra comum na cidade
  - FAQ específica da cidade
  - serviços mais buscados na região
Ex St. Albert: "Drywall contractor in St. Albert for basement renovations,
  garage finishing and residential repairs."
Tarefa Claude Code:
  "In pages/bodies.py give each city its own unique intro paragraph, a short list of
   local neighbourhoods, and 2-3 city-specific FAQ items. Avoid duplicate content."
AÇÃO RUBENS: confirmar bairros/áreas reais de cada cidade se quiser precisão.

## 6. PÁGINAS POR SERVIÇO (serviço + cidade) — SEO máximo
Criar páginas individuais:
  /services/drywall-installation-edmonton.html
  /services/drywall-repair-edmonton.html
  /services/drywall-taping-edmonton.html
  /services/steel-framing-edmonton.html
  /services/interior-painting-edmonton.html
  /services/texture-ceiling-edmonton.html
  /services/insulation-edmonton.html
Tarefa Claude Code:
  "Add a SERVICES_SEO list and a service-page generator in build.py that creates one
   page per service (drywall installation, repair, taping, steel framing, interior
   painting, texture/ceiling, insulation) targeting Edmonton, each with unique title,
   H1, intro, FAQ and CTA. Add them to sitemap.xml."

====================================================================
DEPENDE DO RUBENS / RODRIGO (fora do código)
====================================================================
- [ ] Google Business Profile (criar/reivindicar) — MAIOR fonte de cliente local
- [ ] Fotos reais de obras (antes/depois) para galeria + og:image
- [ ] Depoimentos reais do Google (substituir os placeholder em bodies.py -> testimonials())
- [ ] Confirmar slogan: "One Wall a Time" (logo) vs "One Wall at a Time" (site)
- [ ] Google Search Console + (opcional) Google Analytics / Tag Manager
- [ ] Web3Forms access key
- [ ] Domínio (summitwallsolutions.ca?) — atualizar SITE em build.py, sitemap, robots, canonical

====================================================================
JÁ FEITO ✅
====================================================================
- Estrutura multi-página + CSS/JS separados
- 5 páginas principais + 5 páginas de cidade
- Identidade: Playfair + Lora, paleta maroon/branco/charcoal, logo real
- Header/footer compartilhados via build.py
- robots.txt + sitemap.xml
- Favicon completo (ico, png, apple-touch, android-chrome, manifest)
- Menu legível em todas as páginas (branco no hero escuro, escuro no creme)
- Logo do header maior (58px) e à esquerda

PRÓXIMO PASSO IMEDIATO: Rubens sobe pro GitHub (comandos no chat), depois começamos a lista acima na ordem.

====================================================================
⚠️ ATUALIZAÇÃO DE SERVIÇOS (confirmado pelo Rubens — fonte: Rodrigo)
====================================================================
A lista OFICIAL e ATUAL de serviços (usar EXATAMENTE estes nomes):
  1. Steel Stud Framing
  2. Drywall Installation
  3. Taping and Finishing
  4. Insulation
  5. Painting
  6. Site Cleanup        <-- NOVO (combina com o diferencial "Clean Jobsite Daily")

REMOVER do site: "Texture" (Rodrigo não oferece mais).

Renomear os atuais:
  - "Steel Frame"      -> "Steel Stud Framing"
  - "Drywall"          -> "Drywall Installation"
  - "Taping & Mudding" -> "Taping and Finishing"
  - "Insulation"       -> (manter)
  - "Painting"         -> (manter)
  - "Texture"          -> REMOVER, substituir por "Site Cleanup"

ONDE ISSO IMPACTA (atualizar em TODOS):
  - pages/bodies.py -> lista SERVICES (cards de serviço) [home, services, city pages]
  - pages/bodies.py -> calculadora (chips de serviço + remover rate de 'texture',
    adicionar lógica/preço para 'Site Cleanup' OU tratar cleanup como item sem m2)
  - build.py -> footer (lista de serviços) + qualquer menção
  - tags dentro dos cards de serviço
  - páginas por serviço (tarefa 6) usar estes nomes:
      steel-stud-framing-edmonton, drywall-installation-edmonton,
      taping-and-finishing-edmonton, insulation-edmonton,
      painting-edmonton, (sem texture)
  - meta descriptions que citam "texture"

NOTA calculadora: "Site Cleanup" não é cobrado por sq ft como os outros.
Decidir amanhã: ou tirar da calculadora, ou tratar como add-on fixo/incluído.

Tarefa Claude Code:
  "Update the services everywhere to this exact list: Steel Stud Framing, Drywall
   Installation, Taping and Finishing, Insulation, Painting, Site Cleanup. Remove
   'Texture' completely (cards, calculator rates/chips, footer, tags, meta text).
   Update pages/bodies.py SERVICES list, the calculator in main.js + bodies.py, and
   the footer in build.py. For Site Cleanup in the calculator, treat it as a no-sqft
   item (don't multiply by area). Rebuild and confirm no 'Texture' remains anywhere."

====================================================================
⚠️ ATUALIZAÇÕES DO EMAIL OFICIAL DO RODRIGO (confirmado pelo Rubens)
====================================================================
Fonte: email real que o Rodrigo enviou a um cliente (Todd). É a voz oficial dele.

## A) EMAIL + DOMÍNIO  (substituir em TODO o site)
  - Email NOVO/oficial:  Rodrigo@summitwallsolutions.com
    REMOVER:             Summitwallsolutions@gmail.com  (antigo, não usar mais)
  - Domínio oficial: summitwallsolutions.COM  (é .com, NÃO .ca)
    Atualizar:
      * build.py -> SITE = "https://summitwallsolutions.com"
      * sitemap.xml (todas as URLs .com)
      * robots.txt (Sitemap: .com)
      * canonical de todas as páginas
      * og:url / og:image absolutas
  Onde trocar o email: build.py (footer, header se houver), pages/bodies.py
  (contato), schema JSON-LD, mailto links, meta. Buscar e substituir
  "Summitwallsolutions@gmail.com" -> "Rodrigo@summitwallsolutions.com".

## B) NOME COMPLETO
  - Usar: Rodrigo Gadelha Bandeira  (estava "Rodrigo Gadelha")
    Onde: about.html (fundador), cartão/assinatura, schema (founder/name),
    footer copyright. Pode manter "Rodrigo Gadelha" em contextos curtos, mas o
    nome completo é Rodrigo Gadelha Bandeira.

## C) TIPOS DE PROJETO (usar a linguagem dele — ótimo p/ SEO e conteúdo)
  Residential · Commercial · Tenant Improvement · Basement Development · Renovation
  Usar em: hero/intro, about, páginas de serviço e cidade, schema (areaServed/
  serviceType), meta. "Basement Development" e "Tenant Improvement" são termos
  muito buscados no mercado de Edmonton.

## D) POSICIONAMENTO B2B / SUBCONTRACTOR  (NOVO público-alvo — destacar!)
  Rodrigo também atua como SUBCONTRATADO para construtoras/GCs. O site hoje só
  fala com cliente final. Adicionar uma seção/página voltada a empreiteiras:
    - "Reliable subcontractor for GCs & builders"
    - oferta: full drywall packages, framing crews, finishing work,
      additional manpower to keep projects on schedule
    - foco: quality workmanship, meeting schedules, clear communication
    - CTA: "Request a subcontractor quote" / "Send our company profile"
  Ideia: nova página "for-contractors.html" (ou seção na home) + item no menu.
  Tarefa Claude Code:
    "Add a B2B/subcontractor section (or a for-contractors.html page using the
     shared template) targeting general contractors and builders in Edmonton.
     Highlight: full drywall packages, framing crews, finishing work, extra
     manpower to keep projects on schedule, WCB + liability insurance, quality
     workmanship, meeting schedules, clear communication. Add a clear CTA to
     request a subcontractor quote / company profile. Add to nav + sitemap."

## E) SEGUROS  (atualizar)
  Mencionar BOTH:  WCB coverage  +  Liability insurance
  Hoje o site só diz "WCB Insured". Atualizar ticker, badges, FAQ e schema:
  ex. "WCB + Liability Insured".

## F) VALORES / COPY (palavras do próprio Rodrigo — usar no About e B2B)
  "quality workmanship, meeting schedules, and clear communication"
  "professional, dependable service on every project"

Tarefa Claude Code (resumo desta seção):
  "Global replace: email -> Rodrigo@summitwallsolutions.com; domain -> 
   summitwallsolutions.com (SITE in build.py, sitemap, robots, canonicals).
   Founder full name -> Rodrigo Gadelha Bandeira. Add project types (Residential,
   Commercial, Tenant Improvement, Basement Development, Renovation) into copy and
   schema. Update insurance to 'WCB + Liability'. Then rebuild."

====================================================================
⚠️ EMAILS (decisão Rubens) — DOIS emails, propósitos diferentes
====================================================================
- contact@summitwallsolutions.com  -> PÚBLICO/GERAL: usar no footer, página de
  contato, formulário (campo "to"), e como email principal exibido no site.
- Rodrigo@summitwallsolutions.com   -> CONTATO DIRETO: usar no About (fundador) e
  na seção/página B2B (subcontractor) para GCs falarem direto com o Rodrigo.

ATENÇÃO: na última limpeza setamos TUDO para Rodrigo@. Reabrir e ajustar:
  - footer (build.py) + página contact + formulário  -> contact@summitwallsolutions.com
  - About + B2B page  -> Rodrigo@summitwallsolutions.com
  - schema: email principal = contact@ ; founder/contactPoint pode citar Rodrigo@
Tarefa Claude Code:
  "Use TWO emails: contact@summitwallsolutions.com as the public/general address
   (footer, contact page, the form's destination, schema main email) and
   Rodrigo@summitwallsolutions.com as the direct line (About founder + the B2B/
   for-contractors page). Update accordingly and rebuild."

====================================================================
📷 IMAGENS REAIS (usar no site) — pendente otimizar p/ WebP
====================================================================
Recebidas do Rubens (fotos com a marca aplicada em obra real — ótima prova social):
  1. VAN na obra — ATENÇÃO: versão recebida tem dados ANTIGOS (gmail, @summitwallsolutions,
     "Texture"). Rubens vai gerar versão corrigida em outra IA. Aguardar a nova.
  2. JOB SITE SIGN (placa) na obra — JÁ ESTÁ CORRETA:
        - Serviços certos (Painting | Site Cleanup, sem Texture)
        - Instagram certo (@summitwallsolutins)
        - "Serving Edmonton & Surrounding Areas"
        - "WCB Insured · Quality Guaranteed"
        - tagline secundário "Building Quality. Delivering Trust."
        - email exibido: contact@summitwallsolutions.com
     -> PODE USAR JÁ.

Onde usar as imagens (em vários lugares):
  - Hero da home (foto de fundo levemente escurecida OU bloco lateral)
  - Seção Sobre / "Serving Edmonton & area"
  - Seção/página B2B (van+placa na obra = trabalha com construtoras)
  - og:image + twitter:image (compartilhamento em redes/WhatsApp)

Tarefas:
  A) Otimizar: converter para WebP comprimido (e manter um JPG/PNG fallback).
     Guardar em /assets. Ex: assets/sign-jobsite.webp, assets/van.webp
  B) Tarefa Claude Code (depois que as imagens estiverem em /assets):
     "Add the real photos (assets/sign-jobsite.webp, assets/van.webp) to the site:
      a darkened hero background or side image on the home hero, a photo block in the
      About/service-area section, and on the for-contractors page. Set og:image and
      twitter:image in build.py head() to an absolute URL of one of these. Use
      loading=lazy and width/height to avoid layout shift. Rebuild."
  C) Possível tagline secundário no site: "Building Quality. Delivering Trust."
     (da placa) — usar como subtítulo em alguma seção.

NOTA: a tagline secundária da placa diz "Quality Guaranteed" — alinhado com a
garantia de 1 ano que já está no site. Manter consistente.
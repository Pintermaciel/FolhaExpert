-- Adicionar coluna "valor_inss"
ALTER TABLE competencia ADD COLUMN valor_inss varchar(150);

-- Adicionar coluna "valor_irrf"
ALTER TABLE competencia ADD COLUMN valor_irrf varchar(150);

-- Adicionar coluna "cafe"
ALTER TABLE competencia ADD COLUMN cafe varchar(150);

-- Adicionar coluna "marmita"
ALTER TABLE competencia ADD COLUMN marmita varchar(150);

-- Adicionar coluna "os"
ALTER TABLE competencia ADD COLUMN os varchar(150);

-- Adicionar coluna "multas"
ALTER TABLE competencia ADD COLUMN multas varchar(150);

-- Adicionar coluna "pensao"
ALTER TABLE competencia ADD COLUMN pensao varchar(150);

-- Adicionar coluna "plantao"
ALTER TABLE competencia ADD COLUMN plantao varchar(150);

-- Adicionar coluna "deslocamento"
ALTER TABLE competencia ADD COLUMN deslocamento varchar(150);

-- Adicionar coluna "reb_desp_viagens"
ALTER TABLE competencia ADD COLUMN reb_desp_viagens varchar(150);

-- Adicionar coluna "outros_descontos"
ALTER TABLE competencia ADD COLUMN outros_descontos varchar(150);

-- Adicionar coluna "outros_recebimentos"
ALTER TABLE competencia ADD COLUMN outros_recebimentos varchar(150);

-- Adicionar coluna "valor_pag_deposito"
ALTER TABLE competencia ADD COLUMN valor_pag_deposito varchar(150);

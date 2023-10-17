select  sum(tothr)over() as totgeralhr,* from (
 with geral as (
     with dadosgeral as (
select CASE WHEN NOT (SEQ in(0) AND TP in(1, 2)) THEN row_number()over(partition by codorp_pai,codorp order by seq,tp,codorp,codorp_pai, descripromov) ELSE 0 END as tipoheader ,
case when (CASE WHEN NOT (SEQ in(0) AND TP in(1, 2)) THEN row_number()over(partition by codorp_pai,codorp order by seq,tp,codorp,codorp_pai, descripromov)  END) = 1
 then (totopfilha) end as tot1,* from (  with geral as (

select * from (  with dados2 as (
        with RECURSIVE dados as (
          select 1 as tp,codorp::text as titulo, codorp as codorp_pai, id_ordemproducao as id_pai, codpro ,descripro as descripro, id_produto, 
           qtdproducaoorp ,id_ordemproducao,codorp ,null::INT AS ordprodfilho_id,observorp ,abrevuni,reforp,pedidoorp_id
           --, 0.00 as valormov, null::text as doctomov, 0.00 as qtdademov,null::int as numeromov
           from ordemproducao
            left join produto on  id_produto = codproorp_id
            left join unidade on id_unidade = unidpro_id  

            where 1=1 
            --:pordpro 
            union
            select (select count (*) from (select row_number()over() as seq,regexp_split_to_table( translate(titulo||'.'||opfil.codorp,'.',','), ',')) as sel)::int as tp,
            titulo||'.'||opfil.codorp as analiticas,codorp_pai, id_pai, prod.codpro, prod.descripro, prod.id_produto, opfil.qtdproducaoorp, opfil.id_ordemproducao, 
               opfil.codorp, opfil.ordprodpai_id, opfil.observorp, uni.abrevuni,opfil.reforp,dados.pedidoorp_id

            from  ordemproducao  opfil                          
                  join dados on  opfil.ordprodpai_id = dados.id_ordemproducao
                  left join produto prod on  prod.id_produto = opfil.codproorp_id
            left join unidade uni on uni.id_unidade = unidpro_id 
		            where 1=1 
            --:popmaefilha	
         
)   
            select * from dados  order by  titulo )

          SELECT 1 as tpordem, 0 as seq,
            tp,titulo,codorp, codorp_pai, id_pai, dados2.codpro ,dados2.descripro, dados2.id_produto, 
        dados2.qtdproducaoorp ,dados2.id_ordemproducao,
        ordprodfilho_id,dados2.observorp ,dados2.abrevuni,0 as totopfilha,0::int as ttt,
        NULL::TEXT as abrevunimov,0 as estoque, 0.00 AS valunimov, 
        0.00 AS valormov, NULL::TEXT AS doctomov,0.00  as qtdademovlanc,
         0.00  as qtdademovdev, 0 AS numeromov,NULL::date as dataproducao, NULL::TEXT codpromov, NULL::TEXT as descripromov,pedidoorp_id
    FROM DADOS2  WHERE TP=1
 UNION
         
          SELECT 1 as tpordem, 1  as seq,
            tp,titulo, codorp,codorp_pai, id_pai, dados2.codpro ,dados2.descripro,dados2.id_produto,  
        dados2.qtdproducaoorp- qtentmov ,dados2.id_ordemproducao,
        ordprodfilho_id,observorp ,dados2.abrevuni,0 as totopfilha,0,
        NULL::TEXT as abrevunimov,0 as estoque, 0.00 AS valunimov, 
        0.00 AS valormov, NULL::TEXT AS doctomov,0.00  as qtdademovlanc,
         0.00  as qtdademovdev, 0 AS numeromov,NULL::date as dataproducao, NULL::TEXT codpromov, NULL::TEXT as descripromov,pedidoorp_id
    FROM DADOS2  
LEFT JOIN movimpro  ON  ordemproducao_id = id_ordemproducao and codpromov_id = id_produto  and movimpro.doctomov= ' OP: '||CODORP
WHERE TP=2
UNION
   SELECT 2 as tpordem,1  as seq,
           2 as tp,titulo, codorp,codorp_pai, id_pai, dados2.codpro ,dados2.descripro, dados2.id_produto, 
        dados2.qtdproducaoorp ,dados2.id_ordemproducao,
        ordprodfilho_id, split_part(observorp,':',2) ,dados2.abrevuni,
       sum(sum(case when tipomov = 'E' then -valormov else valormov end))over(partition by id_ordemproducao,ordprodfilho_id order by id_ordemproducao,ordprodfilho_id)as totopfilha,0,
        NULL::TEXT as abrevunimov,0 as estoque, 0.00 AS valunimov, 
        0.00 AS valormov, dados2.reforp AS doctomov,sum(case when tipomov = 'S' then movimpro.qtdademov  else 0.00 end) as qtdademovlanc,
        sum(case when tipomov = 'E' then movimpro.qtdademov else 0.00 end) as qtdademovdev, 0 AS numeromov,NULL::date as dataproducao, NULL::TEXT codpromov, NULL::TEXT as descripromov,pedidoorp_id
    FROM DADOS2  
    LEFT JOIN movimpro  ON movimpro.doctomov= ' OP: '||CODORP
    LEFT Join  produto pro on  pro.id_produto = codpromov_id
    left join unidade on id_unidade = pro.unidpro_id 
    left join estoques on id_estoques = estoquemov_id
    WHERE TP=3 and 1=1
    group by titulo, codorp,codorp_pai, id_pai, dados2.codpro ,dados2.descripro,dados2.id_produto,  
        dados2.qtdproducaoorp ,dados2.id_ordemproducao,
        ordprodfilho_id,split_part(observorp,':',2) ,dados2.abrevuni,tp,dados2.reforp,pedidoorp_id
    UNION all
               SELECT 1 as tpordem, 3 as seq,
        tp,titulo, codorp,codorp as codorp_pai, id_pai, dados2.codpro ,dados2.descripro, dados2.id_produto, 
        dados2.qtdproducaoorp ,dados2.id_ordemproducao,
        ordprodfilho_id,dados2.observorp ,dados2.abrevuni,
sum(case when tipomov = 'E' then -valormov else valormov end)over(partition by id_ordemproducao,ordprodfilho_id order by id_ordemproducao,ordprodfilho_id)as totopfilha,0,
        unidade.abrevuni as abrevunimov,codest as estoque, movimpro.valunimov, 
        case when tipomov = 'E' then -movimpro.valormov else movimpro.valormov end as valormov, movimpro.doctomov,case when tipomov = 'S' then movimpro.qtdademov  else 0.00 end as qtdademovlanc,
        case when tipomov = 'E' then movimpro.qtdademov else 0.00 end as qtdademovdev,
        movimpro.numeromov,datamov::date as dataproducao, pro.codpro as codpromov, pro.descripro as descripromov,pedidoorp_id
    FROM DADOS2 
    LEFT JOIN movimpro  ON movimpro.doctomov= ' OP: '||CODORP
    LEFT Join  produto pro on  pro.id_produto = codpromov_id
    left join unidade on id_unidade = pro.unidpro_id 
    left join estoques on id_estoques = estoquemov_id
    
    WHERE tp in (2)
 UNION
               SELECT 1 as tpordem, 4 as seq,
        tp,titulo, codorp,codorp_pai, id_pai, dados2.codpro ,dados2.descripro, dados2.id_produto, 
        dados2.qtdproducaoorp ,dados2.id_ordemproducao,
         split_part(titulo,'.',2)::int  as ordprodfilho_id,dados2.observorp ,dados2.abrevuni,sum(valormov)over(partition by id_ordemproducao,codorp,ordprodfilho_id order by tp,codorp_pai)as totopfilha,0,
        unidade.abrevuni as abrevunimov,codest as estoque, movimpro.valunimov, 
        movimpro.valormov, movimpro.doctomov,case when tipomov = 'S' then movimpro.qtdademov  else 0.00 end as qtdademovlanc,
        case when tipomov = 'E' then movimpro.qtdademov else 0.00 end as qtdademovdev,
        movimpro.numeromov,datamov::date as dataproducao, pro.codpro as codpromov, pro.descripro as descripromov,pedidoorp_id
    FROM DADOS2 
    LEFT JOIN movimpro  ON movimpro.doctomov= ' OP: '||CODORP
    LEFT Join  produto pro on  pro.id_produto = codpromov_id
    left join unidade on id_unidade = pro.unidpro_id 
    left join estoques on id_estoques = estoquemov_id
    
    WHERE tp in (3)

   order by seq,tp,codorp,codorp_pai,codpromov) as sel  )
select  * from geral --where 1=:ctiporel
   union
      select tpordem, seq,  tp, titulo, codorp, codorp_pai, id_pai, codpro, descripro, id_produto,  sum(qtdproducaoorp), id_ordemproducao, ordprodfilho_id, codorp::text as observorp, abrevuni, totopfilha, 
      ttt, abrevunimov,0 as estoque, 
--case when case when  sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)) < 0 then sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0))*-1 else  sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)) end> 0 then
      --sum(((case when  (coalesce(qtdademovlanc,0))-(coalesce(qtdademovdev,0)) < 0 then (coalesce(qtdademovlanc,0))-(coalesce(qtdademovdev,0))*-1 else  (coalesce(qtdademovlanc,0))-(coalesce(qtdademovdev,0)) end
      --)*(valunimov::numeric(15,2))))/
--case when  sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)) < 0 then sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0))*-1 else  sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)) end
--else  0.00 end as valunimov
case when sum(qtdademovdev+qtdademovlanc)> 0 then
      coalesce(sum(((case when  (coalesce(qtdademovlanc,0))-(coalesce(qtdademovdev,0)) < 0 then (coalesce(qtdademovlanc,0))-(coalesce(qtdademovdev,0))*-1 else  (coalesce(qtdademovlanc,0))-(coalesce(qtdademovdev,0)) end
      )*(valunimov::numeric(15,2)))),1)/
sum(qtdademovdev+qtdademovlanc) end as valunimov
, case when sum(valormov) < 0 then sum(valormov)*-1 else sum(valormov)end as valormov ,null::text as doctomov1, 
--case when  sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)) < 0 then sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0))*-1 else  sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)) end,                                                --Comentado pelo chamado 227621 e adicionado a linha abaixo
sum(coalesce(qtdademovlanc,0))-sum(coalesce(qtdademovdev,0)),         --Adicionado pelo chamado 227621 e comentado a linha acima
sum(coalesce(qtdademovlanc,0)) as qtdademovdev, null::int as numeromov, null::date as dataproducao, codpromov, descripromov,pedidoorp_id   

       from geral --where :ctiporel in(2,3)
       group by seq,  tp, titulo, codorp, codorp_pai, id_pai, codpro, descripro,id_produto,   id_ordemproducao, ordprodfilho_id,  abrevuni, totopfilha, 
      ttt, abrevunimov,  codpromov, descripromov ,tpordem,pedidoorp_id
) AS TTTT
 order by  tipoheader) --:cordem
select  case when valormov < 0 then valormov*-1 else valormov end as valormov,1 as tiporel,sum(tot1)over(partition by codorp)as totopai,*,0 as ids, null::time as hrtrabalhada, 0.00 as tothr
  from dadosgeral  
  left join (select id_pedido,pedidoped,codcli,razsoccli from pedido 
               left join clientes on id_clientes = codcliped_id ) as pedido on pedido.id_pedido = pedidoorp_id
  where 1=1 
  union
  select distinct 0.00 as valormov,7 as tiporel,0.00 as totopai,7 as  tipoheader, 0.00 as tot1, 2 as tpordem,7 as seq,7 as  tp, null::text as  titulo, ordemproducao.codorp, 0 as codorp_pai, id_pai,
        codfun::text as  codpro, nomefun::text as  descripro,id_produto,
        0.00 as qtdproducaoorp,  dadosgeral.id_ordemproducao,0 as  ordprodfilho_id, null::text as observorp, null::text as abrevuni, 0 as totopfilha, ttt, null::text as abrevunimov,0 as  estoque, 0.00 as valunimov, 
         0.00 as valormov_1, null::text as doctomov, 0 as qtdademovlanc,0 as qtdademovdev, 0 as numeromov, null::date as dataproducao,null::text as codpromov, null::text as descripromov,0 as pedidoorp_id,
          0 as id_pedido, null::text as pedidoped,0 as codcli, null::text as  razsoccli,  
           ordemproducaoopf_id   , 
           (justify_hours(to_char((dthrfimopf::time),'HH24:MI:SS')::time-to_char((dthrinicioopf::time),'HH24:MI:SS')::time)::time)::time as totquebra3,  --Alterado via chamado 241691
((extract(hour from (((justify_hours(to_char((dthrfimopf::time),'HH24:MI:SS')::time-to_char((dthrinicioopf::time),'HH24:MI:SS')::time)::time)::time)*60))/60)*valorfco) as totgeral       --Alterado via chamado 241691                                      
                 from dadosgeral
                   inner join ordemproducao on ordemproducao.id_ordemproducao = dadosgeral.id_ordemproducao
                 inner join ordemproducaofunc on  ordemproducaoopf_id =ordemproducao.id_ordemproducao                            
                 left join funcionario on id_funcionario = funcionarioopf_id
  left join funcao on id_funcao = cargofun_id                  
                 
                  where 1=1 order by id_ordemproducao,codpro -- 5707,5708,5709,6965,6984
                  )select * from geral
 order by  tipoheader,tpordem) as sel --:cordem
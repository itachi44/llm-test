db_metadata = {
    "mesx": "La base de données 'mesx' dans postgres contient toutes les informations relatives aux pièces produites dans les industries. Parfois dans les tables il est nécéssaire de faire des jointures pour avoir toutes les données.",
    "prod": "La base de données 'prod' dans postgres contient toutes les informations relatives aux données de l'application digitale. Parfois dans les tables il est nécéssaire de faire des jointures pour avoir toutes les données."
}

table_descriptions = {
    "mesx": {
        "di_cycle": "Contient les informations les quantité de pièces produites à chaque cycle",
        "di_production_status": "Fournit le statut de la production pour chaque données tag de machine",
        "di_scrap": "Contient données sur les rebuts ou pièces rejetées lors de la production, avec leurs quantités",
        "oi_operation": "Contient les détails des opérations des opérateurs de saisies",
        "oi_production_settings": "Stocke les paramètres de configuration de la production, tels que les réglages des machines",
        "oi_scrap": "Contient les données liées aux rebuts des pièces saisies par les opérateurs : rebuts saisies par les opérateurs",
        "oi_status": "Suivi des statuts des différentes opérations dans le processus de production : saisie par les opérateurs",
        "machine": "Contient les informations sur les machines utilisées dans les processus de fabrication",
        "machine_status": "Fournit le statut en temps réel des machines",
        "machine_tag": "Associe des tags aux machines pour un suivi ou une identification simplifiée",
        "machine_workplace": "Associe les machines aux postes de travail ou emplacements dans l'usine.",
        "tag": "Stocke les informations sur les tags utilisés dans le système (identifiants pour les objets, machines, etc.)."
    },
    "prod": {
        "alerts": "Contient les alertes générées par l'application digitale, y compris les informations sur leur type et leur date.",
        "comments": "Stocke les commentaires ajoutés par les utilisateurs dans le cadre d'incidents ou d'opérations.",
        "documents": "Liste les documents partagés ou attachés aux différents processus de l'application.",
        "groups": "Contient les informations sur les groupes d'utilisateurs définis dans le système.",
        "groups_users": "Fait le lien entre les groupes et leurs membres (utilisateurs).",
        "incidents": "Liste les incidents enregistrés, avec leurs descriptions et statuts.",
        "incidents_answers": "Stocke les réponses ou informations collectées pour résoudre les incidents.",
        "incidents_models": "Détaille les modèles ou types d'incidents préenregistrés.",
        "incidents_node_answers": "Associe les réponses aux questions ou nœuds spécifiques des incidents.",
        "incidents_node_questions": "Stocke les questions associées aux incidents pour guider leur résolution.",
        "input_data": "Enregistre les données saisies par les utilisateurs via l'application.",
        "instructions": "Détaille les instructions ou consignes liées aux opérations ou incidents.",
        "master_sessions": "Contient les informations sur les ordres de fabrication",
        "master_sessions_attachments": "Stocke les fichiers ou documents attachés aux ordres de fabrications",
        "operations2": "Détaille les opérations réalisées, y compris leurs paramètres et résultats.",
        "products": "Stocke les informations sur les produits fabriqués gérés dans l'application.",
        "reports": "Contient les rapports que doivent remplir les opérateurs leur de leur travail",
        "role_permissions": "Détaille les permissions associées aux différents rôles dans le système.",
        "roles": "Contient les rôles définis dans l'application pour gérer les droits d'accès.",
        "sessions": "Ce sont les sessions liées aux master sessions",
        "sessions_attachments": "Stocke les pièces jointes ou documents associés aux sessions.",
        "status": "Contient les statuts généraux des entités gérées dans le système.",
        "work_orders": "Liste les ordres de fabrication de produit, avec leurs détails et statuts.",
        "workplaces": "Détaille les postes de travail ou emplacements utilisés dans les opérations."
    }
}


query_examples = {
    "mesx": [
        {
            "question": "Quels sont les statuts des machines pour un client et un site spécifique ?",
            "sql": """
                SELECT * 
                FROM machine_status 
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quels tags sont associés aux machines pour un client et un site donné ?",
            "sql": """
                SELECT machine_tag.tag_id, machine_tag.machine_id
                FROM machine_tag
                JOIN machine ON machine.id = machine_tag.machine_id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quelles quantités ont été produites lors des cycles de production pour un client et un site donné ?",
            "sql": """
                SELECT di_cycle.id, di_cycle.tag_id, di_cycle.timestamp, di_cycle.quantity
                FROM di_cycle
                JOIN tag ON di_cycle.tag_id = tag.id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quels sont les statuts de production associés aux tags pour un client et un site donné ?",
            "sql": """
                SELECT di_production_status.id, di_production_status.tag_id,
                       di_production_status.timestamp, di_production_status.status
                FROM di_production_status
                JOIN tag ON di_production_status.tag_id = tag.id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Combien de rebuts ont été produits pour un client et un site spécifique ?",
            "sql": """
                SELECT di_scrap.id, di_scrap.tag_id, di_scrap.timestamp, di_scrap.quantity
                FROM di_scrap
                JOIN tag ON di_scrap.tag_id = tag.id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quels sont les postes de travail associés aux machines pour un client et un site spécifique ?",
            "sql": """
                SELECT machine_workplace.workplace_id, machine_workplace.machine_id
                FROM machine_workplace
                JOIN machine ON machine.id = machine_workplace.machine_id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quels sont les paramètres de configuration de production pour un client et un site donné ?",
            "sql": """
                SELECT oi_production_settings.id, oi_production_settings.machine_id,
                       oi_production_settings.operator_id, oi_production_settings.timestamp,
                       oi_production_settings.cycle_time_ms, oi_production_settings.items_per_cycle
                FROM oi_production_settings
                JOIN machine ON machine.id = oi_production_settings.machine_id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Combien de déchets ont été générés lors des opérations pour un client et un site donné ?",
            "sql": """
                SELECT oi_scrap.id, oi_scrap.machine_id, oi_scrap.operator_id,
                       oi_scrap.timestamp, oi_scrap.quantity
                FROM oi_scrap
                JOIN machine ON machine.id = oi_scrap.machine_id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quels sont les statuts des opérations pour un client et un site spécifique ?",
            "sql": """
                SELECT oi_status.id, oi_status.machine_id, oi_status.operator_id,
                       oi_status.timestamp, oi_status.status_id, oi_status.comment,
                       oi_status.replaced_by_oi_status_id
                FROM oi_status
                JOIN machine ON machine.id = oi_status.machine_id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quelles opérations ont été effectuées pour un client et un site donné ?",
            "sql": """
                SELECT oi_operation.id, oi_operation.operator_id, oi_operation.timestamp,
                       oi_operation.master_session_id, oi_operation.status, oi_operation.workplace_id
                FROM oi_operation
                JOIN machine_workplace ON oi_operation.workplace_id = machine_workplace.workplace_id
                JOIN machine ON machine.id = machine_workplace.machine_id
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
        {
            "question": "Quels sont les tags associés à un client et un site spécifique ?",
            "sql": """
                SELECT *
                FROM tag
                WHERE client_id = 'test' AND site_id = 'test'
            """
        },
    {
        "question": "Récupère les arrêts machines de la veille.",
        "sql": """
            WITH machine_data_ps AS (
                SELECT 
                    m.id AS machine_id,
                    m.label AS label_machine,
                    (NOW()::DATE - INTERVAL '1 day')::timestamp AS analysis_start,
                    (NOW()::DATE)::timestamp AS analysis_end
                FROM machine m
                WHERE m.client_id = 'test'
                  AND m.site_id = 'test'
                  AND m.data_mode = 'status+cycle'
            ),
            machine_data_eoc AS (
                SELECT 
                    m.id AS machine_id,
                    m.label AS label_machine,
                    (NOW()::DATE - INTERVAL '1 day')::timestamp AS analysis_start,
                    (NOW()::DATE)::timestamp AS analysis_end
                FROM machine m
                WHERE m.client_id = 'test'
                  AND m.site_id = 'test'
                  AND m.data_mode != 'status+cycle'
            ),
            timeline_data_ps AS (
                SELECT 
                    md.machine_id,
                    md.label_machine,
                    COALESCE(ms.start, NOW()::timestamp)::timestamp AS stoppage_start,
                    COALESCE(ms."end", NOW()::timestamp)::timestamp AS stoppage_end,
                    ms.machine_status AS stoppage_type,
                    EXTRACT(EPOCH FROM (COALESCE(ms."end", NOW()) - COALESCE(ms.start, NOW()))) AS stoppage_duration
                FROM machine_data_ps md
                CROSS JOIN LATERAL (
                    SELECT *
                    FROM srf_machine_status_timeline_ps(
                        md.machine_id, 
                        md.analysis_start, 
                        md.analysis_end
                    ) ms
                    WHERE ms.machine_status NOT IN ('production', 'unknown', 'Available')
                ) ms
            ),
            timeline_data_eoc AS (
                SELECT 
                    md.machine_id,
                    md.label_machine,
                    COALESCE(ms.start, NOW()::timestamp)::timestamp AS stoppage_start,
                    COALESCE(ms."end", NOW()::timestamp)::timestamp AS stoppage_end,
                    ms.machine_status AS stoppage_type,
                    EXTRACT(EPOCH FROM (COALESCE(ms."end", NOW()) - COALESCE(ms.start, NOW()))) AS stoppage_duration
                FROM machine_data_eoc md
                CROSS JOIN LATERAL (
                    SELECT *
                    FROM srf_machine_status_timeline_eoc(
                        md.machine_id, 
                        md.analysis_start, 
                        md.analysis_end
                    ) ms
                    WHERE ms.machine_status NOT IN ('production', 'unknown', 'Available')
                ) ms
            ),
            combined_timeline_data AS (
                SELECT * FROM timeline_data_ps
                UNION ALL
                SELECT * FROM timeline_data_eoc
            )
            SELECT 
                combined_timeline_data.machine_id,
                combined_timeline_data.label_machine,
                combined_timeline_data.stoppage_type,
                combined_timeline_data.stoppage_start,
                combined_timeline_data.stoppage_end,
                combined_timeline_data.stoppage_duration
            FROM 
                combined_timeline_data
            ORDER BY 
                combined_timeline_data.stoppage_start DESC;
        """
    },
        {
            "question": "Compte les rebuts de pièces de la veille.",
            "sql": """
                SELECT COALESCE(SUM(ds.quantity), 0) AS total_scraps
                FROM di_scrap ds
                JOIN tag t ON ds.tag_id = t.id
                WHERE t.client_id = 'test' AND t.site_id = 'test'
                  AND ds.timestamp >= NOW() - INTERVAL '1 day'
                  AND ds.timestamp < NOW();
            """
        },
        {
            "question": "Récupère le nombre de pièces produites la veille.",
            "sql": """
                SELECT COALESCE(SUM(di_cycle.quantity), 0) AS total_quantity
                FROM di_cycle
                JOIN tag ON di_cycle.tag_id = tag.id
                WHERE tag.client_id = 'test' AND tag.site_id = 'test'
                  AND di_cycle.timestamp >= NOW() - INTERVAL '1 day'
                  AND di_cycle.timestamp < NOW();
            """
        },
        {
            "question": "Récupère les informations sur l'ordre de fabrication (OF) pour savoir s'il y a du retard ou de l'avance.",
            "sql": """
                SELECT EXTRACT(EPOCH FROM (update_date - start_date)) / 3600 AS time_difference
                FROM master_sessions
                WHERE client_id = 'test' AND site_id = 'test' AND production_order_id = 'test';
            """
        },
    {
        "question": "Récupère les indicateurs de performance de la veille (TRS, performance, qualité, disponibilité).",
        "sql": """
            WITH machine_data AS (
                SELECT 
                    m.id AS machine_id,
                    m.label AS label_machine,
                    m.data_mode,
                    NOW()::DATE - INTERVAL '1 day' AS analysis_start,
                    NOW()::DATE AS analysis_end
                FROM machine m
                WHERE m.client_id = 'test'
                  AND m.site_id = 'test'
            ),
            trs_calculation AS (
                SELECT 
                    md.machine_id,
                    md.label_machine,
                    CASE 
                        WHEN md.data_mode = 'status+cycle' THEN (
                            SELECT oee
                            FROM srf_oee_for_machine_ps(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                        ELSE (
                            SELECT oee
                            FROM srf_oee_for_machine_eoc(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                    END AS trs_metric,
                    CASE 
                        WHEN md.data_mode = 'status+cycle' THEN (
                            SELECT availability
                            FROM srf_oee_for_machine_ps(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                        ELSE (
                            SELECT availability
                            FROM srf_oee_for_machine_eoc(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                    END AS availability_metric,
                    CASE 
                        WHEN md.data_mode = 'status+cycle' THEN (
                            SELECT performance
                            FROM srf_oee_for_machine_ps(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                        ELSE (
                            SELECT performance
                            FROM srf_oee_for_machine_eoc(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                    END AS performance_metric,
                    CASE 
                        WHEN md.data_mode = 'status+cycle' THEN (
                            SELECT quality
                            FROM srf_oee_for_machine_ps(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                        ELSE (
                            SELECT quality
                            FROM srf_oee_for_machine_eoc(
                                md.machine_id, 
                                md.analysis_start, 
                                md.analysis_end
                            )
                        )
                    END AS quality_metric
                FROM machine_data md
            )
            SELECT 
                machine_id,
                label_machine,
                trs_metric,
                performance_metric,
                quality_metric,
                availability_metric
            FROM trs_calculation;
        """
    },
        {
            "question": "Récupère les consignes de la veille.",
            "sql": """
                SELECT comment AS instruction_comment
                FROM instructions
                WHERE client_id = 'test' AND site_id = 'test'
                  AND is_deleted = FALSE
                  AND creation_date >= NOW() - INTERVAL '1 day'
                  AND creation_date < NOW();
            """
        }
    ],
    "prod": [

    ]
}


PRODUCTION_SOURCE = [
  {
    "WorkorderID": 1,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator115, Operator61, Operator29, Operator9",
    "Tooling": "Tool29, Tool26, Tool25",
    "BatchSize": 63,
    "Quantity": 771
  },
  {
    "WorkorderID": 1,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 14:14",
    "EndDateTime": "2024-10-01 19:14",
    "Process": "Preparing",
    "Operators": "Operator21, Operator15, Operator57, Operator58, Operator105",
    "Tooling": "Tool8",
    "BatchSize": 63,
    "Quantity": 771
  },
  {
    "WorkorderID": 1,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 18:23",
    "EndDateTime": "2024-10-03 00:23",
    "Process": "Silver Plating",
    "Operators": "Operator15, Operator36",
    "Tooling": "Tool13, Tool27",
    "BatchSize": 63,
    "Quantity": 771
  },
  {
    "WorkorderID": 1,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 06:10",
    "EndDateTime": "2024-10-03 08:10",
    "Process": "Polishing",
    "Operators": "Operator107, Operator88, Operator5, Operator60",
    "Tooling": "Tool22, Tool6",
    "BatchSize": 63,
    "Quantity": 771
  },
  {
    "WorkorderID": 1,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 12:03",
    "EndDateTime": "2024-10-03 17:03",
    "Process": "Conditioning",
    "Operators": "Operator124, Operator29, Operator126, Operator109, Operator48",
    "Tooling": "Tool30",
    "BatchSize": 63,
    "Quantity": 771
  },
  {
    "WorkorderID": 2,
    "Product": "Bowl",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator94, Operator105, Operator114, Operator28",
    "Tooling": "Tool30",
    "BatchSize": 113,
    "Quantity": 623
  },
  {
    "WorkorderID": 2,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 12:04",
    "EndDateTime": "2024-10-01 19:04",
    "Process": "Preparing",
    "Operators": "Operator103",
    "Tooling": "Tool7",
    "BatchSize": 113,
    "Quantity": 623
  },
  {
    "WorkorderID": 2,
    "Product": "Bowl",
    "StartDateTime": "2024-10-02 12:15",
    "EndDateTime": "2024-10-02 20:15",
    "Process": "Silver Plating",
    "Operators": "Operator50, Operator122, Operator148",
    "Tooling": "Tool28, Tool3, Tool6",
    "BatchSize": 113,
    "Quantity": 623
  },
  {
    "WorkorderID": 2,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 01:35",
    "EndDateTime": "2024-10-03 03:35",
    "Process": "Polishing",
    "Operators": "Operator23, Operator3, Operator40, Operator44, Operator57",
    "Tooling": "Tool11",
    "BatchSize": 113,
    "Quantity": 623
  },
  {
    "WorkorderID": 2,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 14:02",
    "EndDateTime": "2024-10-03 18:02",
    "Process": "Conditioning",
    "Operators": "Operator133, Operator72, Operator94, Operator117",
    "Tooling": "Tool16, Tool11, Tool14",
    "BatchSize": 113,
    "Quantity": 623
  },
  {
    "WorkorderID": 3,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator24",
    "Tooling": "Tool1, Tool30, Tool18",
    "BatchSize": 132,
    "Quantity": 1310
  },
  {
    "WorkorderID": 3,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 01:53",
    "EndDateTime": "2024-10-02 03:53",
    "Process": "Preparing",
    "Operators": "Operator64, Operator127, Operator111, Operator25, Operator12",
    "Tooling": "Tool24, Tool3, Tool12",
    "BatchSize": 132,
    "Quantity": 1310
  },
  {
    "WorkorderID": 3,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 12:09",
    "EndDateTime": "2024-10-02 13:09",
    "Process": "Silver Plating",
    "Operators": "Operator47",
    "Tooling": "Tool4, Tool10, Tool24",
    "BatchSize": 132,
    "Quantity": 1310
  },
  {
    "WorkorderID": 3,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 20:18",
    "EndDateTime": "2024-10-03 01:18",
    "Process": "Polishing",
    "Operators": "Operator60, Operator106",
    "Tooling": "Tool23, Tool24, Tool8",
    "BatchSize": 132,
    "Quantity": 1310
  },
  {
    "WorkorderID": 3,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 05:27",
    "EndDateTime": "2024-10-03 07:27",
    "Process": "Conditioning",
    "Operators": "Operator60, Operator92, Operator124, Operator33",
    "Tooling": "Tool21, Tool27, Tool12",
    "BatchSize": 132,
    "Quantity": 1310
  },
  {
    "WorkorderID": 4,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator122, Operator4, Operator67, Operator99",
    "Tooling": "Tool5, Tool17, Tool6",
    "BatchSize": 68,
    "Quantity": 1176
  },
  {
    "WorkorderID": 4,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 13:34",
    "EndDateTime": "2024-10-01 17:34",
    "Process": "Preparing",
    "Operators": "Operator76, Operator91, Operator98, Operator14, Operator131",
    "Tooling": "Tool24, Tool5, Tool14",
    "BatchSize": 68,
    "Quantity": 1176
  },
  {
    "WorkorderID": 4,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 21:14",
    "EndDateTime": "2024-10-02 01:14",
    "Process": "Silver Plating",
    "Operators": "Operator143, Operator39",
    "Tooling": "Tool26, Tool2",
    "BatchSize": 68,
    "Quantity": 1176
  },
  {
    "WorkorderID": 4,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 16:38",
    "EndDateTime": "2024-10-02 20:38",
    "Process": "Polishing",
    "Operators": "Operator133, Operator64, Operator62, Operator42",
    "Tooling": "Tool26",
    "BatchSize": 68,
    "Quantity": 1176
  },
  {
    "WorkorderID": 4,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 09:27",
    "EndDateTime": "2024-10-03 17:27",
    "Process": "Conditioning",
    "Operators": "Operator128, Operator114",
    "Tooling": "Tool1, Tool2",
    "BatchSize": 68,
    "Quantity": 1176
  },
  {
    "WorkorderID": 5,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator122",
    "Tooling": "Tool8, Tool19",
    "BatchSize": 60,
    "Quantity": 1053
  },
  {
    "WorkorderID": 5,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 08:01",
    "EndDateTime": "2024-10-01 11:01",
    "Process": "Preparing",
    "Operators": "Operator21",
    "Tooling": "Tool15, Tool16",
    "BatchSize": 60,
    "Quantity": 1053
  },
  {
    "WorkorderID": 5,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 05:46",
    "EndDateTime": "2024-10-02 12:46",
    "Process": "Silver Plating",
    "Operators": "Operator133, Operator67, Operator17, Operator50",
    "Tooling": "Tool4, Tool24",
    "BatchSize": 60,
    "Quantity": 1053
  },
  {
    "WorkorderID": 5,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 19:52",
    "EndDateTime": "2024-10-03 01:52",
    "Process": "Polishing",
    "Operators": "Operator147, Operator63, Operator66",
    "Tooling": "Tool29, Tool4, Tool3",
    "BatchSize": 60,
    "Quantity": 1053
  },
  {
    "WorkorderID": 5,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 17:02",
    "EndDateTime": "2024-10-03 21:02",
    "Process": "Conditioning",
    "Operators": "Operator141, Operator31",
    "Tooling": "Tool16, Tool4, Tool26",
    "BatchSize": 60,
    "Quantity": 1053
  },
  {
    "WorkorderID": 6,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator150, Operator63, Operator5, Operator13, Operator28",
    "Tooling": "Tool9, Tool26",
    "BatchSize": 60,
    "Quantity": 999
  },
  {
    "WorkorderID": 6,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 05:08",
    "EndDateTime": "2024-10-01 10:08",
    "Process": "Preparing",
    "Operators": "Operator108, Operator10",
    "Tooling": "Tool20",
    "BatchSize": 60,
    "Quantity": 999
  },
  {
    "WorkorderID": 6,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 20:13",
    "EndDateTime": "2024-10-01 22:13",
    "Process": "Silver Plating",
    "Operators": "Operator68, Operator22, Operator13, Operator89",
    "Tooling": "Tool16, Tool13",
    "BatchSize": 60,
    "Quantity": 999
  },
  {
    "WorkorderID": 6,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 16:57",
    "EndDateTime": "2024-10-02 20:57",
    "Process": "Polishing",
    "Operators": "Operator24, Operator5, Operator143, Operator121, Operator21",
    "Tooling": "Tool24, Tool4, Tool12",
    "BatchSize": 60,
    "Quantity": 999
  },
  {
    "WorkorderID": 6,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 02:40",
    "EndDateTime": "2024-10-03 10:40",
    "Process": "Conditioning",
    "Operators": "Operator57, Operator85, Operator14, Operator21, Operator95",
    "Tooling": "Tool5, Tool9, Tool20",
    "BatchSize": 60,
    "Quantity": 999
  },
  {
    "WorkorderID": 7,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator148, Operator138",
    "Tooling": "Tool21, Tool30, Tool20",
    "BatchSize": 72,
    "Quantity": 1234
  },
  {
    "WorkorderID": 7,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 22:25",
    "EndDateTime": "2024-10-02 02:25",
    "Process": "Preparing",
    "Operators": "Operator83, Operator85, Operator108, Operator123",
    "Tooling": "Tool20, Tool30",
    "BatchSize": 72,
    "Quantity": 1234
  },
  {
    "WorkorderID": 7,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 10:37",
    "EndDateTime": "2024-10-02 15:37",
    "Process": "Silver Plating",
    "Operators": "Operator123, Operator98",
    "Tooling": "Tool5, Tool25, Tool11",
    "BatchSize": 72,
    "Quantity": 1234
  },
  {
    "WorkorderID": 7,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 09:22",
    "EndDateTime": "2024-10-03 10:22",
    "Process": "Polishing",
    "Operators": "Operator49, Operator51",
    "Tooling": "Tool30, Tool14",
    "BatchSize": 72,
    "Quantity": 1234
  },
  {
    "WorkorderID": 7,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 17:37",
    "EndDateTime": "2024-10-04 01:37",
    "Process": "Conditioning",
    "Operators": "Operator109, Operator24, Operator36, Operator51",
    "Tooling": "Tool7, Tool27",
    "BatchSize": 72,
    "Quantity": 1234
  },
  {
    "WorkorderID": 8,
    "Product": "Chalice",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator55, Operator51, Operator116, Operator34, Operator60",
    "Tooling": "Tool28, Tool19, Tool22",
    "BatchSize": 133,
    "Quantity": 1250
  },
  {
    "WorkorderID": 8,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 01:40",
    "EndDateTime": "2024-10-02 03:40",
    "Process": "Preparing",
    "Operators": "Operator101, Operator56",
    "Tooling": "Tool14",
    "BatchSize": 133,
    "Quantity": 1250
  },
  {
    "WorkorderID": 8,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 09:09",
    "EndDateTime": "2024-10-02 14:09",
    "Process": "Silver Plating",
    "Operators": "Operator54, Operator140, Operator35",
    "Tooling": "Tool4, Tool8",
    "BatchSize": 133,
    "Quantity": 1250
  },
  {
    "WorkorderID": 8,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 15:46",
    "EndDateTime": "2024-10-02 23:46",
    "Process": "Polishing",
    "Operators": "Operator14, Operator74, Operator64, Operator46",
    "Tooling": "Tool13, Tool9, Tool26",
    "BatchSize": 133,
    "Quantity": 1250
  },
  {
    "WorkorderID": 8,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 04:11",
    "EndDateTime": "2024-10-03 11:11",
    "Process": "Conditioning",
    "Operators": "Operator11, Operator81, Operator51, Operator59, Operator87",
    "Tooling": "Tool20, Tool1",
    "BatchSize": 133,
    "Quantity": 1250
  },
  {
    "WorkorderID": 9,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator127, Operator39, Operator66, Operator58",
    "Tooling": "Tool19",
    "BatchSize": 119,
    "Quantity": 600
  },
  {
    "WorkorderID": 9,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 12:25",
    "EndDateTime": "2024-10-01 15:25",
    "Process": "Preparing",
    "Operators": "Operator105, Operator135, Operator72, Operator95",
    "Tooling": "Tool27, Tool4, Tool25",
    "BatchSize": 119,
    "Quantity": 600
  },
  {
    "WorkorderID": 9,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 07:27",
    "EndDateTime": "2024-10-02 10:27",
    "Process": "Silver Plating",
    "Operators": "Operator17, Operator80, Operator105",
    "Tooling": "Tool18, Tool9",
    "BatchSize": 119,
    "Quantity": 600
  },
  {
    "WorkorderID": 9,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 00:11",
    "EndDateTime": "2024-10-03 04:11",
    "Process": "Polishing",
    "Operators": "Operator44, Operator28, Operator9, Operator84",
    "Tooling": "Tool18",
    "BatchSize": 119,
    "Quantity": 600
  },
  {
    "WorkorderID": 9,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 08:47",
    "EndDateTime": "2024-10-03 10:47",
    "Process": "Conditioning",
    "Operators": "Operator123",
    "Tooling": "Tool19, Tool18",
    "BatchSize": 119,
    "Quantity": 600
  },
  {
    "WorkorderID": 10,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator96",
    "Tooling": "Tool23",
    "BatchSize": 124,
    "Quantity": 1001
  },
  {
    "WorkorderID": 10,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 13:55",
    "EndDateTime": "2024-10-01 20:55",
    "Process": "Preparing",
    "Operators": "Operator12",
    "Tooling": "Tool25, Tool29, Tool8",
    "BatchSize": 124,
    "Quantity": 1001
  },
  {
    "WorkorderID": 10,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 23:34",
    "EndDateTime": "2024-10-02 00:34",
    "Process": "Silver Plating",
    "Operators": "Operator119, Operator18, Operator67",
    "Tooling": "Tool8, Tool3",
    "BatchSize": 124,
    "Quantity": 1001
  },
  {
    "WorkorderID": 10,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 12:09",
    "EndDateTime": "2024-10-02 17:09",
    "Process": "Polishing",
    "Operators": "Operator124, Operator55, Operator90",
    "Tooling": "Tool22",
    "BatchSize": 124,
    "Quantity": 1001
  },
  {
    "WorkorderID": 10,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 15:34",
    "EndDateTime": "2024-10-03 21:34",
    "Process": "Conditioning",
    "Operators": "Operator11, Operator56, Operator105",
    "Tooling": "Tool19",
    "BatchSize": 124,
    "Quantity": 1001
  },
  {
    "WorkorderID": 11,
    "Product": "Chalice",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator143, Operator125, Operator25, Operator14, Operator90",
    "Tooling": "Tool19, Tool30, Tool24",
    "BatchSize": 127,
    "Quantity": 930
  },
  {
    "WorkorderID": 11,
    "Product": "Chalice",
    "StartDateTime": "2024-10-01 09:50",
    "EndDateTime": "2024-10-01 12:50",
    "Process": "Preparing",
    "Operators": "Operator91, Operator103, Operator52",
    "Tooling": "Tool19",
    "BatchSize": 127,
    "Quantity": 930
  },
  {
    "WorkorderID": 11,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 04:28",
    "EndDateTime": "2024-10-02 05:28",
    "Process": "Silver Plating",
    "Operators": "Operator108, Operator139",
    "Tooling": "Tool1, Tool13",
    "BatchSize": 127,
    "Quantity": 930
  },
  {
    "WorkorderID": 11,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 12:48",
    "EndDateTime": "2024-10-02 14:48",
    "Process": "Polishing",
    "Operators": "Operator14",
    "Tooling": "Tool14",
    "BatchSize": 127,
    "Quantity": 930
  },
  {
    "WorkorderID": 11,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 13:57",
    "EndDateTime": "2024-10-03 15:57",
    "Process": "Conditioning",
    "Operators": "Operator111, Operator19, Operator32",
    "Tooling": "Tool27, Tool6",
    "BatchSize": 127,
    "Quantity": 930
  },
  {
    "WorkorderID": 12,
    "Product": "Chalice",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator128, Operator133, Operator26, Operator43, Operator87",
    "Tooling": "Tool11, Tool3, Tool13",
    "BatchSize": 112,
    "Quantity": 645
  },
  {
    "WorkorderID": 12,
    "Product": "Chalice",
    "StartDateTime": "2024-10-01 19:55",
    "EndDateTime": "2024-10-01 21:55",
    "Process": "Preparing",
    "Operators": "Operator10",
    "Tooling": "Tool17, Tool28",
    "BatchSize": 112,
    "Quantity": 645
  },
  {
    "WorkorderID": 12,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 11:23",
    "EndDateTime": "2024-10-02 15:23",
    "Process": "Silver Plating",
    "Operators": "Operator144, Operator22, Operator46, Operator33",
    "Tooling": "Tool3, Tool17, Tool5",
    "BatchSize": 112,
    "Quantity": 645
  },
  {
    "WorkorderID": 12,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 00:06",
    "EndDateTime": "2024-10-03 08:06",
    "Process": "Polishing",
    "Operators": "Operator70, Operator46, Operator92, Operator58",
    "Tooling": "Tool4",
    "BatchSize": 112,
    "Quantity": 645
  },
  {
    "WorkorderID": 12,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 20:37",
    "EndDateTime": "2024-10-04 02:37",
    "Process": "Conditioning",
    "Operators": "Operator112, Operator118, Operator52",
    "Tooling": "Tool9, Tool21",
    "BatchSize": 112,
    "Quantity": 645
  },
  {
    "WorkorderID": 13,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator87, Operator77, Operator22, Operator110, Operator47",
    "Tooling": "Tool12",
    "BatchSize": 136,
    "Quantity": 1032
  },
  {
    "WorkorderID": 13,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 20:16",
    "EndDateTime": "2024-10-02 04:16",
    "Process": "Preparing",
    "Operators": "Operator146, Operator45",
    "Tooling": "Tool21",
    "BatchSize": 136,
    "Quantity": 1032
  },
  {
    "WorkorderID": 13,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 22:26",
    "EndDateTime": "2024-10-03 02:26",
    "Process": "Silver Plating",
    "Operators": "Operator134",
    "Tooling": "Tool19, Tool26, Tool7",
    "BatchSize": 136,
    "Quantity": 1032
  },
  {
    "WorkorderID": 13,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 11:19",
    "EndDateTime": "2024-10-03 17:19",
    "Process": "Polishing",
    "Operators": "Operator78, Operator32, Operator52, Operator10",
    "Tooling": "Tool5",
    "BatchSize": 136,
    "Quantity": 1032
  },
  {
    "WorkorderID": 13,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-04 11:46",
    "EndDateTime": "2024-10-04 13:46",
    "Process": "Conditioning",
    "Operators": "Operator129, Operator138, Operator53",
    "Tooling": "Tool1, Tool22",
    "BatchSize": 136,
    "Quantity": 1032
  },
  {
    "WorkorderID": 14,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator120, Operator47, Operator89",
    "Tooling": "Tool6, Tool14, Tool2",
    "BatchSize": 104,
    "Quantity": 636
  },
  {
    "WorkorderID": 14,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 19:50",
    "EndDateTime": "2024-10-01 20:50",
    "Process": "Preparing",
    "Operators": "Operator31",
    "Tooling": "Tool6",
    "BatchSize": 104,
    "Quantity": 636
  },
  {
    "WorkorderID": 14,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 11:19",
    "EndDateTime": "2024-10-02 18:19",
    "Process": "Silver Plating",
    "Operators": "Operator29, Operator98",
    "Tooling": "Tool1, Tool11, Tool25",
    "BatchSize": 104,
    "Quantity": 636
  },
  {
    "WorkorderID": 14,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 00:59",
    "EndDateTime": "2024-10-03 01:59",
    "Process": "Polishing",
    "Operators": "Operator130, Operator94, Operator70, Operator52, Operator129",
    "Tooling": "Tool4, Tool23",
    "BatchSize": 104,
    "Quantity": 636
  },
  {
    "WorkorderID": 14,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 12:44",
    "EndDateTime": "2024-10-03 18:44",
    "Process": "Conditioning",
    "Operators": "Operator138, Operator3, Operator99, Operator132, Operator31",
    "Tooling": "Tool22, Tool4",
    "BatchSize": 104,
    "Quantity": 636
  },
  {
    "WorkorderID": 15,
    "Product": "Bowl",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator27, Operator118, Operator113",
    "Tooling": "Tool9, Tool13",
    "BatchSize": 79,
    "Quantity": 1247
  },
  {
    "WorkorderID": 15,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 20:25",
    "EndDateTime": "2024-10-02 01:25",
    "Process": "Preparing",
    "Operators": "Operator147, Operator123, Operator136, Operator109",
    "Tooling": "Tool7",
    "BatchSize": 79,
    "Quantity": 1247
  },
  {
    "WorkorderID": 15,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 00:17",
    "EndDateTime": "2024-10-03 07:17",
    "Process": "Silver Plating",
    "Operators": "Operator17, Operator38",
    "Tooling": "Tool26",
    "BatchSize": 79,
    "Quantity": 1247
  },
  {
    "WorkorderID": 15,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 09:55",
    "EndDateTime": "2024-10-03 13:55",
    "Process": "Polishing",
    "Operators": "Operator4, Operator95",
    "Tooling": "Tool20",
    "BatchSize": 79,
    "Quantity": 1247
  },
  {
    "WorkorderID": 15,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 19:14",
    "EndDateTime": "2024-10-03 23:14",
    "Process": "Conditioning",
    "Operators": "Operator87, Operator38, Operator107, Operator130, Operator28",
    "Tooling": "Tool20, Tool9",
    "BatchSize": 79,
    "Quantity": 1247
  },
  {
    "WorkorderID": 16,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator122, Operator91",
    "Tooling": "Tool6, Tool18, Tool20",
    "BatchSize": 100,
    "Quantity": 1458
  },
  {
    "WorkorderID": 16,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 01:23",
    "EndDateTime": "2024-10-02 07:23",
    "Process": "Preparing",
    "Operators": "Operator132, Operator86",
    "Tooling": "Tool25, Tool24",
    "BatchSize": 100,
    "Quantity": 1458
  },
  {
    "WorkorderID": 16,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 02:52",
    "EndDateTime": "2024-10-03 04:52",
    "Process": "Silver Plating",
    "Operators": "Operator53, Operator139, Operator60, Operator76",
    "Tooling": "Tool28",
    "BatchSize": 100,
    "Quantity": 1458
  },
  {
    "WorkorderID": 16,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 05:37",
    "EndDateTime": "2024-10-03 11:37",
    "Process": "Polishing",
    "Operators": "Operator126, Operator140",
    "Tooling": "Tool1",
    "BatchSize": 100,
    "Quantity": 1458
  },
  {
    "WorkorderID": 16,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 17:49",
    "EndDateTime": "2024-10-03 21:49",
    "Process": "Conditioning",
    "Operators": "Operator30, Operator35",
    "Tooling": "Tool14",
    "BatchSize": 100,
    "Quantity": 1458
  },
  {
    "WorkorderID": 17,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator50",
    "Tooling": "Tool6, Tool19",
    "BatchSize": 100,
    "Quantity": 737
  },
  {
    "WorkorderID": 17,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 10:25",
    "EndDateTime": "2024-10-01 16:25",
    "Process": "Preparing",
    "Operators": "Operator68, Operator135, Operator11, Operator45",
    "Tooling": "Tool18, Tool21",
    "BatchSize": 100,
    "Quantity": 737
  },
  {
    "WorkorderID": 17,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 11:38",
    "EndDateTime": "2024-10-02 15:38",
    "Process": "Silver Plating",
    "Operators": "Operator53, Operator82, Operator42",
    "Tooling": "Tool16, Tool23, Tool24",
    "BatchSize": 100,
    "Quantity": 737
  },
  {
    "WorkorderID": 17,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 02:47",
    "EndDateTime": "2024-10-03 09:47",
    "Process": "Polishing",
    "Operators": "Operator95",
    "Tooling": "Tool3",
    "BatchSize": 100,
    "Quantity": 737
  },
  {
    "WorkorderID": 17,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 15:06",
    "EndDateTime": "2024-10-03 20:06",
    "Process": "Conditioning",
    "Operators": "Operator133, Operator25, Operator39, Operator37, Operator31",
    "Tooling": "Tool15",
    "BatchSize": 100,
    "Quantity": 737
  },
  {
    "WorkorderID": 18,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator60, Operator22, Operator13",
    "Tooling": "Tool9, Tool12",
    "BatchSize": 112,
    "Quantity": 1139
  },
  {
    "WorkorderID": 18,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 10:53",
    "EndDateTime": "2024-10-01 16:53",
    "Process": "Preparing",
    "Operators": "Operator108",
    "Tooling": "Tool18, Tool21",
    "BatchSize": 112,
    "Quantity": 1139
  },
  {
    "WorkorderID": 18,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 09:14",
    "EndDateTime": "2024-10-02 10:14",
    "Process": "Silver Plating",
    "Operators": "Operator52, Operator36, Operator70, Operator45",
    "Tooling": "Tool21",
    "BatchSize": 112,
    "Quantity": 1139
  },
  {
    "WorkorderID": 18,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 08:28",
    "EndDateTime": "2024-10-03 12:28",
    "Process": "Polishing",
    "Operators": "Operator52, Operator143, Operator41",
    "Tooling": "Tool10",
    "BatchSize": 112,
    "Quantity": 1139
  },
  {
    "WorkorderID": 18,
    "Product": "Teapot",
    "StartDateTime": "2024-10-04 11:53",
    "EndDateTime": "2024-10-04 12:53",
    "Process": "Conditioning",
    "Operators": "Operator19",
    "Tooling": "Tool26, Tool2",
    "BatchSize": 112,
    "Quantity": 1139
  },
  {
    "WorkorderID": 19,
    "Product": "Chalice",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator21, Operator33, Operator38, Operator105, Operator137",
    "Tooling": "Tool25",
    "BatchSize": 105,
    "Quantity": 1144
  },
  {
    "WorkorderID": 19,
    "Product": "Chalice",
    "StartDateTime": "2024-10-01 15:04",
    "EndDateTime": "2024-10-01 22:04",
    "Process": "Preparing",
    "Operators": "Operator141",
    "Tooling": "Tool13, Tool4",
    "BatchSize": 105,
    "Quantity": 1144
  },
  {
    "WorkorderID": 19,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 01:10",
    "EndDateTime": "2024-10-02 05:10",
    "Process": "Silver Plating",
    "Operators": "Operator51, Operator125, Operator138",
    "Tooling": "Tool23",
    "BatchSize": 105,
    "Quantity": 1144
  },
  {
    "WorkorderID": 19,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 02:48",
    "EndDateTime": "2024-10-03 08:48",
    "Process": "Polishing",
    "Operators": "Operator51, Operator23, Operator20, Operator117, Operator140",
    "Tooling": "Tool28, Tool16, Tool24",
    "BatchSize": 105,
    "Quantity": 1144
  },
  {
    "WorkorderID": 19,
    "Product": "Chalice",
    "StartDateTime": "2024-10-04 04:47",
    "EndDateTime": "2024-10-04 05:47",
    "Process": "Conditioning",
    "Operators": "Operator57, Operator116, Operator88, Operator71",
    "Tooling": "Tool11, Tool26, Tool17",
    "BatchSize": 105,
    "Quantity": 1144
  },
  {
    "WorkorderID": 20,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator12, Operator78, Operator132, Operator107, Operator41",
    "Tooling": "Tool26",
    "BatchSize": 96,
    "Quantity": 862
  },
  {
    "WorkorderID": 20,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 02:49",
    "EndDateTime": "2024-10-02 09:49",
    "Process": "Preparing",
    "Operators": "Operator104, Operator69, Operator74, Operator18",
    "Tooling": "Tool17, Tool28",
    "BatchSize": 96,
    "Quantity": 862
  },
  {
    "WorkorderID": 20,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 04:04",
    "EndDateTime": "2024-10-03 11:04",
    "Process": "Silver Plating",
    "Operators": "Operator17, Operator144, Operator94, Operator102, Operator59",
    "Tooling": "Tool1",
    "BatchSize": 96,
    "Quantity": 862
  },
  {
    "WorkorderID": 20,
    "Product": "Jug",
    "StartDateTime": "2024-10-04 00:27",
    "EndDateTime": "2024-10-04 05:27",
    "Process": "Polishing",
    "Operators": "Operator17",
    "Tooling": "Tool30",
    "BatchSize": 96,
    "Quantity": 862
  },
  {
    "WorkorderID": 20,
    "Product": "Jug",
    "StartDateTime": "2024-10-05 04:33",
    "EndDateTime": "2024-10-05 11:33",
    "Process": "Conditioning",
    "Operators": "Operator68, Operator145, Operator142, Operator19, Operator139",
    "Tooling": "Tool3, Tool20, Tool4",
    "BatchSize": 96,
    "Quantity": 862
  },
  {
    "WorkorderID": 21,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator68, Operator104, Operator26, Operator123",
    "Tooling": "Tool8, Tool27",
    "BatchSize": 70,
    "Quantity": 1257
  },
  {
    "WorkorderID": 21,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 06:46",
    "EndDateTime": "2024-10-01 09:46",
    "Process": "Preparing",
    "Operators": "Operator18",
    "Tooling": "Tool6",
    "BatchSize": 70,
    "Quantity": 1257
  },
  {
    "WorkorderID": 21,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 12:47",
    "EndDateTime": "2024-10-01 17:47",
    "Process": "Silver Plating",
    "Operators": "Operator61, Operator86, Operator10, Operator40",
    "Tooling": "Tool9",
    "BatchSize": 70,
    "Quantity": 1257
  },
  {
    "WorkorderID": 21,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 08:37",
    "EndDateTime": "2024-10-02 11:37",
    "Process": "Polishing",
    "Operators": "Operator49",
    "Tooling": "Tool18",
    "BatchSize": 70,
    "Quantity": 1257
  },
  {
    "WorkorderID": 21,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 19:56",
    "EndDateTime": "2024-10-02 23:56",
    "Process": "Conditioning",
    "Operators": "Operator18, Operator118, Operator28, Operator66",
    "Tooling": "Tool23",
    "BatchSize": 70,
    "Quantity": 1257
  },
  {
    "WorkorderID": 22,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator46, Operator101, Operator69, Operator11, Operator53",
    "Tooling": "Tool12, Tool6, Tool28",
    "BatchSize": 89,
    "Quantity": 1101
  },
  {
    "WorkorderID": 22,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 07:13",
    "EndDateTime": "2024-10-01 15:13",
    "Process": "Preparing",
    "Operators": "Operator126, Operator46, Operator80, Operator110, Operator144",
    "Tooling": "Tool1, Tool17, Tool2",
    "BatchSize": 89,
    "Quantity": 1101
  },
  {
    "WorkorderID": 22,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 16:29",
    "EndDateTime": "2024-10-01 21:29",
    "Process": "Silver Plating",
    "Operators": "Operator72, Operator14, Operator101, Operator85, Operator70",
    "Tooling": "Tool22",
    "BatchSize": 89,
    "Quantity": 1101
  },
  {
    "WorkorderID": 22,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 13:47",
    "EndDateTime": "2024-10-02 20:47",
    "Process": "Polishing",
    "Operators": "Operator132, Operator110",
    "Tooling": "Tool6, Tool3",
    "BatchSize": 89,
    "Quantity": 1101
  },
  {
    "WorkorderID": 22,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 22:39",
    "EndDateTime": "2024-10-03 01:39",
    "Process": "Conditioning",
    "Operators": "Operator94, Operator122, Operator91, Operator50",
    "Tooling": "Tool1",
    "BatchSize": 89,
    "Quantity": 1101
  },
  {
    "WorkorderID": 23,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator59, Operator52, Operator117, Operator66",
    "Tooling": "Tool11",
    "BatchSize": 65,
    "Quantity": 645
  },
  {
    "WorkorderID": 23,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 16:31",
    "EndDateTime": "2024-10-02 00:31",
    "Process": "Preparing",
    "Operators": "Operator84, Operator91, Operator24, Operator109",
    "Tooling": "Tool15, Tool24, Tool6",
    "BatchSize": 65,
    "Quantity": 645
  },
  {
    "WorkorderID": 23,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 12:10",
    "EndDateTime": "2024-10-02 18:10",
    "Process": "Silver Plating",
    "Operators": "Operator103, Operator146, Operator134",
    "Tooling": "Tool27, Tool15, Tool8",
    "BatchSize": 65,
    "Quantity": 645
  },
  {
    "WorkorderID": 23,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 15:39",
    "EndDateTime": "2024-10-03 22:39",
    "Process": "Polishing",
    "Operators": "Operator43",
    "Tooling": "Tool12, Tool7, Tool11",
    "BatchSize": 65,
    "Quantity": 645
  },
  {
    "WorkorderID": 23,
    "Product": "Teapot",
    "StartDateTime": "2024-10-04 09:49",
    "EndDateTime": "2024-10-04 16:49",
    "Process": "Conditioning",
    "Operators": "Operator116, Operator146, Operator97, Operator109, Operator130",
    "Tooling": "Tool19, Tool3",
    "BatchSize": 65,
    "Quantity": 645
  },
  {
    "WorkorderID": 24,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator94",
    "Tooling": "Tool4, Tool5",
    "BatchSize": 51,
    "Quantity": 1280
  },
  {
    "WorkorderID": 24,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 02:16",
    "EndDateTime": "2024-10-01 05:16",
    "Process": "Preparing",
    "Operators": "Operator55",
    "Tooling": "Tool15",
    "BatchSize": 51,
    "Quantity": 1280
  },
  {
    "WorkorderID": 24,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 09:17",
    "EndDateTime": "2024-10-01 13:17",
    "Process": "Silver Plating",
    "Operators": "Operator22, Operator128",
    "Tooling": "Tool15, Tool21, Tool10",
    "BatchSize": 51,
    "Quantity": 1280
  },
  {
    "WorkorderID": 24,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 02:17",
    "EndDateTime": "2024-10-02 10:17",
    "Process": "Polishing",
    "Operators": "Operator119, Operator21, Operator46, Operator55",
    "Tooling": "Tool3",
    "BatchSize": 51,
    "Quantity": 1280
  },
  {
    "WorkorderID": 24,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 02:07",
    "EndDateTime": "2024-10-03 05:07",
    "Process": "Conditioning",
    "Operators": "Operator124, Operator80, Operator82",
    "Tooling": "Tool7, Tool1, Tool16",
    "BatchSize": 51,
    "Quantity": 1280
  },
  {
    "WorkorderID": 25,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator11",
    "Tooling": "Tool18",
    "BatchSize": 120,
    "Quantity": 584
  },
  {
    "WorkorderID": 25,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 18:57",
    "EndDateTime": "2024-10-01 19:57",
    "Process": "Preparing",
    "Operators": "Operator37, Operator17, Operator23",
    "Tooling": "Tool7, Tool15",
    "BatchSize": 120,
    "Quantity": 584
  },
  {
    "WorkorderID": 25,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 20:06",
    "EndDateTime": "2024-10-02 02:06",
    "Process": "Silver Plating",
    "Operators": "Operator139, Operator146, Operator27, Operator87",
    "Tooling": "Tool30, Tool7, Tool22",
    "BatchSize": 120,
    "Quantity": 584
  },
  {
    "WorkorderID": 25,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 21:27",
    "EndDateTime": "2024-10-03 04:27",
    "Process": "Polishing",
    "Operators": "Operator78",
    "Tooling": "Tool28",
    "BatchSize": 120,
    "Quantity": 584
  },
  {
    "WorkorderID": 25,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 15:08",
    "EndDateTime": "2024-10-03 19:08",
    "Process": "Conditioning",
    "Operators": "Operator39, Operator62, Operator130, Operator90, Operator13",
    "Tooling": "Tool6, Tool20, Tool19",
    "BatchSize": 120,
    "Quantity": 584
  },
  {
    "WorkorderID": 26,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator110, Operator85, Operator146, Operator62",
    "Tooling": "Tool4",
    "BatchSize": 73,
    "Quantity": 887
  },
  {
    "WorkorderID": 26,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 09:54",
    "EndDateTime": "2024-10-01 15:54",
    "Process": "Preparing",
    "Operators": "Operator78, Operator91, Operator102",
    "Tooling": "Tool16, Tool6",
    "BatchSize": 73,
    "Quantity": 887
  },
  {
    "WorkorderID": 26,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 17:19",
    "EndDateTime": "2024-10-01 20:19",
    "Process": "Silver Plating",
    "Operators": "Operator89, Operator2, Operator110, Operator129",
    "Tooling": "Tool20",
    "BatchSize": 73,
    "Quantity": 887
  },
  {
    "WorkorderID": 26,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 20:45",
    "EndDateTime": "2024-10-02 02:45",
    "Process": "Polishing",
    "Operators": "Operator110, Operator59, Operator112",
    "Tooling": "Tool12, Tool7, Tool24",
    "BatchSize": 73,
    "Quantity": 887
  },
  {
    "WorkorderID": 26,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 08:41",
    "EndDateTime": "2024-10-02 11:41",
    "Process": "Conditioning",
    "Operators": "Operator146",
    "Tooling": "Tool5",
    "BatchSize": 73,
    "Quantity": 887
  },
  {
    "WorkorderID": 27,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator123, Operator19",
    "Tooling": "Tool2, Tool11",
    "BatchSize": 141,
    "Quantity": 903
  },
  {
    "WorkorderID": 27,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 22:51",
    "EndDateTime": "2024-10-02 05:51",
    "Process": "Preparing",
    "Operators": "Operator90, Operator11",
    "Tooling": "Tool16, Tool27",
    "BatchSize": 141,
    "Quantity": 903
  },
  {
    "WorkorderID": 27,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 14:53",
    "EndDateTime": "2024-10-02 18:53",
    "Process": "Silver Plating",
    "Operators": "Operator124, Operator64, Operator129, Operator35",
    "Tooling": "Tool7, Tool4",
    "BatchSize": 141,
    "Quantity": 903
  },
  {
    "WorkorderID": 27,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 05:43",
    "EndDateTime": "2024-10-03 09:43",
    "Process": "Polishing",
    "Operators": "Operator124, Operator56, Operator113",
    "Tooling": "Tool15",
    "BatchSize": 141,
    "Quantity": 903
  },
  {
    "WorkorderID": 27,
    "Product": "Bottle",
    "StartDateTime": "2024-10-04 06:21",
    "EndDateTime": "2024-10-04 13:21",
    "Process": "Conditioning",
    "Operators": "Operator72, Operator61, Operator89, Operator59",
    "Tooling": "Tool23, Tool22, Tool12",
    "BatchSize": 141,
    "Quantity": 903
  },
  {
    "WorkorderID": 28,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator26, Operator7, Operator136, Operator6",
    "Tooling": "Tool27, Tool2",
    "BatchSize": 53,
    "Quantity": 1123
  },
  {
    "WorkorderID": 28,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 04:38",
    "EndDateTime": "2024-10-01 10:38",
    "Process": "Preparing",
    "Operators": "Operator23, Operator125, Operator85, Operator7, Operator30",
    "Tooling": "Tool16",
    "BatchSize": 53,
    "Quantity": 1123
  },
  {
    "WorkorderID": 28,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 16:05",
    "EndDateTime": "2024-10-02 00:05",
    "Process": "Silver Plating",
    "Operators": "Operator35, Operator16",
    "Tooling": "Tool18, Tool5",
    "BatchSize": 53,
    "Quantity": 1123
  },
  {
    "WorkorderID": 28,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 19:48",
    "EndDateTime": "2024-10-03 02:48",
    "Process": "Polishing",
    "Operators": "Operator134",
    "Tooling": "Tool6",
    "BatchSize": 53,
    "Quantity": 1123
  },
  {
    "WorkorderID": 28,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 05:21",
    "EndDateTime": "2024-10-03 07:21",
    "Process": "Conditioning",
    "Operators": "Operator3, Operator125, Operator35, Operator121, Operator10",
    "Tooling": "Tool2",
    "BatchSize": 53,
    "Quantity": 1123
  },
  {
    "WorkorderID": 29,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator134, Operator87",
    "Tooling": "Tool26",
    "BatchSize": 135,
    "Quantity": 527
  },
  {
    "WorkorderID": 29,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 04:05",
    "EndDateTime": "2024-10-02 06:05",
    "Process": "Preparing",
    "Operators": "Operator41, Operator3, Operator150, Operator46",
    "Tooling": "Tool13",
    "BatchSize": 135,
    "Quantity": 527
  },
  {
    "WorkorderID": 29,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 23:43",
    "EndDateTime": "2024-10-03 06:43",
    "Process": "Silver Plating",
    "Operators": "Operator96, Operator29",
    "Tooling": "Tool10, Tool27, Tool11",
    "BatchSize": 135,
    "Quantity": 527
  },
  {
    "WorkorderID": 29,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-04 03:51",
    "EndDateTime": "2024-10-04 04:51",
    "Process": "Polishing",
    "Operators": "Operator90, Operator149",
    "Tooling": "Tool19",
    "BatchSize": 135,
    "Quantity": 527
  },
  {
    "WorkorderID": 29,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-04 05:38",
    "EndDateTime": "2024-10-04 06:38",
    "Process": "Conditioning",
    "Operators": "Operator101",
    "Tooling": "Tool26, Tool15, Tool1",
    "BatchSize": 135,
    "Quantity": 527
  },
  {
    "WorkorderID": 30,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator25, Operator81, Operator104",
    "Tooling": "Tool26",
    "BatchSize": 50,
    "Quantity": 965
  },
  {
    "WorkorderID": 30,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 06:22",
    "EndDateTime": "2024-10-01 12:22",
    "Process": "Preparing",
    "Operators": "Operator125",
    "Tooling": "Tool16, Tool4, Tool18",
    "BatchSize": 50,
    "Quantity": 965
  },
  {
    "WorkorderID": 30,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 08:50",
    "EndDateTime": "2024-10-02 11:50",
    "Process": "Silver Plating",
    "Operators": "Operator84",
    "Tooling": "Tool17, Tool18",
    "BatchSize": 50,
    "Quantity": 965
  },
  {
    "WorkorderID": 30,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 23:21",
    "EndDateTime": "2024-10-03 00:21",
    "Process": "Polishing",
    "Operators": "Operator129, Operator44, Operator39",
    "Tooling": "Tool3, Tool29",
    "BatchSize": 50,
    "Quantity": 965
  },
  {
    "WorkorderID": 30,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-04 00:11",
    "EndDateTime": "2024-10-04 07:11",
    "Process": "Conditioning",
    "Operators": "Operator16, Operator51, Operator75, Operator3",
    "Tooling": "Tool2",
    "BatchSize": 50,
    "Quantity": 965
  },
  {
    "WorkorderID": 31,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator117, Operator149, Operator49, Operator105, Operator90",
    "Tooling": "Tool8",
    "BatchSize": 92,
    "Quantity": 1261
  },
  {
    "WorkorderID": 31,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 07:50",
    "EndDateTime": "2024-10-01 11:50",
    "Process": "Preparing",
    "Operators": "Operator75, Operator22, Operator131",
    "Tooling": "Tool10",
    "BatchSize": 92,
    "Quantity": 1261
  },
  {
    "WorkorderID": 31,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 13:23",
    "EndDateTime": "2024-10-01 17:23",
    "Process": "Silver Plating",
    "Operators": "Operator78, Operator42",
    "Tooling": "Tool8, Tool14",
    "BatchSize": 92,
    "Quantity": 1261
  },
  {
    "WorkorderID": 31,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 21:31",
    "EndDateTime": "2024-10-01 22:31",
    "Process": "Polishing",
    "Operators": "Operator139, Operator115, Operator77",
    "Tooling": "Tool19, Tool27, Tool7",
    "BatchSize": 92,
    "Quantity": 1261
  },
  {
    "WorkorderID": 31,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 22:33",
    "EndDateTime": "2024-10-02 05:33",
    "Process": "Conditioning",
    "Operators": "Operator22",
    "Tooling": "Tool7, Tool20, Tool12",
    "BatchSize": 92,
    "Quantity": 1261
  },
  {
    "WorkorderID": 32,
    "Product": "Chalice",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator134, Operator102, Operator57, Operator46",
    "Tooling": "Tool3, Tool4",
    "BatchSize": 97,
    "Quantity": 1261
  },
  {
    "WorkorderID": 32,
    "Product": "Chalice",
    "StartDateTime": "2024-10-01 14:00",
    "EndDateTime": "2024-10-01 22:00",
    "Process": "Preparing",
    "Operators": "Operator118, Operator12, Operator147",
    "Tooling": "Tool25, Tool22, Tool26",
    "BatchSize": 97,
    "Quantity": 1261
  },
  {
    "WorkorderID": 32,
    "Product": "Chalice",
    "StartDateTime": "2024-10-02 07:34",
    "EndDateTime": "2024-10-02 10:34",
    "Process": "Silver Plating",
    "Operators": "Operator146",
    "Tooling": "Tool6, Tool29, Tool2",
    "BatchSize": 97,
    "Quantity": 1261
  },
  {
    "WorkorderID": 32,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 03:10",
    "EndDateTime": "2024-10-03 06:10",
    "Process": "Polishing",
    "Operators": "Operator140, Operator37, Operator40, Operator122, Operator80",
    "Tooling": "Tool6",
    "BatchSize": 97,
    "Quantity": 1261
  },
  {
    "WorkorderID": 32,
    "Product": "Chalice",
    "StartDateTime": "2024-10-03 17:29",
    "EndDateTime": "2024-10-03 22:29",
    "Process": "Conditioning",
    "Operators": "Operator68, Operator96",
    "Tooling": "Tool2, Tool20, Tool7",
    "BatchSize": 97,
    "Quantity": 1261
  },
  {
    "WorkorderID": 33,
    "Product": "Cup",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator137, Operator60",
    "Tooling": "Tool7",
    "BatchSize": 132,
    "Quantity": 1204
  },
  {
    "WorkorderID": 33,
    "Product": "Cup",
    "StartDateTime": "2024-10-01 12:25",
    "EndDateTime": "2024-10-01 18:25",
    "Process": "Preparing",
    "Operators": "Operator4, Operator36, Operator81, Operator60",
    "Tooling": "Tool22, Tool20, Tool21",
    "BatchSize": 132,
    "Quantity": 1204
  },
  {
    "WorkorderID": 33,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 11:19",
    "EndDateTime": "2024-10-02 17:19",
    "Process": "Silver Plating",
    "Operators": "Operator142",
    "Tooling": "Tool22",
    "BatchSize": 132,
    "Quantity": 1204
  },
  {
    "WorkorderID": 33,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 19:01",
    "EndDateTime": "2024-10-02 20:01",
    "Process": "Polishing",
    "Operators": "Operator36, Operator97, Operator28",
    "Tooling": "Tool1",
    "BatchSize": 132,
    "Quantity": 1204
  },
  {
    "WorkorderID": 33,
    "Product": "Cup",
    "StartDateTime": "2024-10-03 06:04",
    "EndDateTime": "2024-10-03 13:04",
    "Process": "Conditioning",
    "Operators": "Operator100, Operator75, Operator136, Operator71, Operator2",
    "Tooling": "Tool14",
    "BatchSize": 132,
    "Quantity": 1204
  },
  {
    "WorkorderID": 34,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator104, Operator59, Operator53, Operator105",
    "Tooling": "Tool11",
    "BatchSize": 140,
    "Quantity": 1398
  },
  {
    "WorkorderID": 34,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 17:14",
    "EndDateTime": "2024-10-01 21:14",
    "Process": "Preparing",
    "Operators": "Operator85",
    "Tooling": "Tool15, Tool26",
    "BatchSize": 140,
    "Quantity": 1398
  },
  {
    "WorkorderID": 34,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 11:59",
    "EndDateTime": "2024-10-02 16:59",
    "Process": "Silver Plating",
    "Operators": "Operator67, Operator93, Operator87, Operator65",
    "Tooling": "Tool14, Tool21, Tool29",
    "BatchSize": 140,
    "Quantity": 1398
  },
  {
    "WorkorderID": 34,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 03:12",
    "EndDateTime": "2024-10-03 10:12",
    "Process": "Polishing",
    "Operators": "Operator90, Operator63, Operator134",
    "Tooling": "Tool28",
    "BatchSize": 140,
    "Quantity": 1398
  },
  {
    "WorkorderID": 34,
    "Product": "Coaster",
    "StartDateTime": "2024-10-04 02:29",
    "EndDateTime": "2024-10-04 06:29",
    "Process": "Conditioning",
    "Operators": "Operator87",
    "Tooling": "Tool18",
    "BatchSize": 140,
    "Quantity": 1398
  },
  {
    "WorkorderID": 35,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator20, Operator37, Operator8",
    "Tooling": "Tool19",
    "BatchSize": 133,
    "Quantity": 644
  },
  {
    "WorkorderID": 35,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 07:38",
    "EndDateTime": "2024-10-01 08:38",
    "Process": "Preparing",
    "Operators": "Operator4, Operator56",
    "Tooling": "Tool6, Tool19, Tool1",
    "BatchSize": 133,
    "Quantity": 644
  },
  {
    "WorkorderID": 35,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 04:23",
    "EndDateTime": "2024-10-02 07:23",
    "Process": "Silver Plating",
    "Operators": "Operator119, Operator79, Operator148, Operator141",
    "Tooling": "Tool22",
    "BatchSize": 133,
    "Quantity": 644
  },
  {
    "WorkorderID": 35,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 20:36",
    "EndDateTime": "2024-10-02 21:36",
    "Process": "Polishing",
    "Operators": "Operator33",
    "Tooling": "Tool30, Tool21",
    "BatchSize": 133,
    "Quantity": 644
  },
  {
    "WorkorderID": 35,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 06:33",
    "EndDateTime": "2024-10-03 09:33",
    "Process": "Conditioning",
    "Operators": "Operator103, Operator87, Operator54",
    "Tooling": "Tool16",
    "BatchSize": 133,
    "Quantity": 644
  },
  {
    "WorkorderID": 36,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator92, Operator80",
    "Tooling": "Tool8, Tool11",
    "BatchSize": 102,
    "Quantity": 826
  },
  {
    "WorkorderID": 36,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 17:01",
    "EndDateTime": "2024-10-01 21:01",
    "Process": "Preparing",
    "Operators": "Operator106, Operator87",
    "Tooling": "Tool8",
    "BatchSize": 102,
    "Quantity": 826
  },
  {
    "WorkorderID": 36,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 17:48",
    "EndDateTime": "2024-10-02 19:48",
    "Process": "Silver Plating",
    "Operators": "Operator146, Operator6, Operator149",
    "Tooling": "Tool8",
    "BatchSize": 102,
    "Quantity": 826
  },
  {
    "WorkorderID": 36,
    "Product": "Knife",
    "StartDateTime": "2024-10-03 02:02",
    "EndDateTime": "2024-10-03 03:02",
    "Process": "Polishing",
    "Operators": "Operator116, Operator9, Operator1, Operator138, Operator79",
    "Tooling": "Tool26",
    "BatchSize": 102,
    "Quantity": 826
  },
  {
    "WorkorderID": 36,
    "Product": "Knife",
    "StartDateTime": "2024-10-03 03:29",
    "EndDateTime": "2024-10-03 04:29",
    "Process": "Conditioning",
    "Operators": "Operator79, Operator123, Operator38",
    "Tooling": "Tool26, Tool15, Tool3",
    "BatchSize": 102,
    "Quantity": 826
  },
  {
    "WorkorderID": 37,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator136, Operator107, Operator98, Operator66, Operator109",
    "Tooling": "Tool14",
    "BatchSize": 134,
    "Quantity": 813
  },
  {
    "WorkorderID": 37,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 23:23",
    "EndDateTime": "2024-10-02 05:23",
    "Process": "Preparing",
    "Operators": "Operator52",
    "Tooling": "Tool30",
    "BatchSize": 134,
    "Quantity": 813
  },
  {
    "WorkorderID": 37,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 03:59",
    "EndDateTime": "2024-10-03 04:59",
    "Process": "Silver Plating",
    "Operators": "Operator133",
    "Tooling": "Tool15",
    "BatchSize": 134,
    "Quantity": 813
  },
  {
    "WorkorderID": 37,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 05:23",
    "EndDateTime": "2024-10-03 09:23",
    "Process": "Polishing",
    "Operators": "Operator2, Operator143",
    "Tooling": "Tool1, Tool24",
    "BatchSize": 134,
    "Quantity": 813
  },
  {
    "WorkorderID": 37,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 16:38",
    "EndDateTime": "2024-10-03 20:38",
    "Process": "Conditioning",
    "Operators": "Operator107, Operator43, Operator12, Operator143",
    "Tooling": "Tool22, Tool8, Tool1",
    "BatchSize": 134,
    "Quantity": 813
  },
  {
    "WorkorderID": 38,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator50, Operator9, Operator46, Operator40",
    "Tooling": "Tool29",
    "BatchSize": 117,
    "Quantity": 1473
  },
  {
    "WorkorderID": 38,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 02:57",
    "EndDateTime": "2024-10-02 05:57",
    "Process": "Preparing",
    "Operators": "Operator14, Operator24, Operator31, Operator118, Operator97",
    "Tooling": "Tool10, Tool1",
    "BatchSize": 117,
    "Quantity": 1473
  },
  {
    "WorkorderID": 38,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 12:33",
    "EndDateTime": "2024-10-02 17:33",
    "Process": "Silver Plating",
    "Operators": "Operator1, Operator126, Operator73, Operator36",
    "Tooling": "Tool10, Tool11",
    "BatchSize": 117,
    "Quantity": 1473
  },
  {
    "WorkorderID": 38,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 01:47",
    "EndDateTime": "2024-10-03 04:47",
    "Process": "Polishing",
    "Operators": "Operator77, Operator147, Operator17, Operator32, Operator62",
    "Tooling": "Tool6",
    "BatchSize": 117,
    "Quantity": 1473
  },
  {
    "WorkorderID": 38,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 15:32",
    "EndDateTime": "2024-10-03 18:32",
    "Process": "Conditioning",
    "Operators": "Operator86",
    "Tooling": "Tool23",
    "BatchSize": 117,
    "Quantity": 1473
  },
  {
    "WorkorderID": 39,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator65, Operator15, Operator93",
    "Tooling": "Tool5, Tool8",
    "BatchSize": 95,
    "Quantity": 596
  },
  {
    "WorkorderID": 39,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 08:30",
    "EndDateTime": "2024-10-01 15:30",
    "Process": "Preparing",
    "Operators": "Operator39, Operator40, Operator21",
    "Tooling": "Tool23, Tool3",
    "BatchSize": 95,
    "Quantity": 596
  },
  {
    "WorkorderID": 39,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 07:05",
    "EndDateTime": "2024-10-02 09:05",
    "Process": "Silver Plating",
    "Operators": "Operator75, Operator10, Operator115, Operator28, Operator4",
    "Tooling": "Tool23, Tool5",
    "BatchSize": 95,
    "Quantity": 596
  },
  {
    "WorkorderID": 39,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 19:37",
    "EndDateTime": "2024-10-03 03:37",
    "Process": "Polishing",
    "Operators": "Operator126, Operator29, Operator127, Operator150, Operator28",
    "Tooling": "Tool20, Tool2, Tool14",
    "BatchSize": 95,
    "Quantity": 596
  },
  {
    "WorkorderID": 39,
    "Product": "Coaster",
    "StartDateTime": "2024-10-04 03:30",
    "EndDateTime": "2024-10-04 10:30",
    "Process": "Conditioning",
    "Operators": "Operator10",
    "Tooling": "Tool12, Tool28",
    "BatchSize": 95,
    "Quantity": 596
  },
  {
    "WorkorderID": 40,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator1, Operator99",
    "Tooling": "Tool30, Tool15, Tool20",
    "BatchSize": 96,
    "Quantity": 596
  },
  {
    "WorkorderID": 40,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 17:24",
    "EndDateTime": "2024-10-01 22:24",
    "Process": "Preparing",
    "Operators": "Operator130, Operator32",
    "Tooling": "Tool8, Tool22, Tool12",
    "BatchSize": 96,
    "Quantity": 596
  },
  {
    "WorkorderID": 40,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 04:43",
    "EndDateTime": "2024-10-02 12:43",
    "Process": "Silver Plating",
    "Operators": "Operator59",
    "Tooling": "Tool17, Tool15",
    "BatchSize": 96,
    "Quantity": 596
  },
  {
    "WorkorderID": 40,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 22:29",
    "EndDateTime": "2024-10-03 02:29",
    "Process": "Polishing",
    "Operators": "Operator149, Operator145, Operator53, Operator48",
    "Tooling": "Tool4, Tool8, Tool26",
    "BatchSize": 96,
    "Quantity": 596
  },
  {
    "WorkorderID": 40,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 10:50",
    "EndDateTime": "2024-10-03 17:50",
    "Process": "Conditioning",
    "Operators": "Operator64, Operator94, Operator48, Operator18, Operator4",
    "Tooling": "Tool23",
    "BatchSize": 96,
    "Quantity": 596
  },
  {
    "WorkorderID": 41,
    "Product": "Cup",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator20",
    "Tooling": "Tool8",
    "BatchSize": 105,
    "Quantity": 836
  },
  {
    "WorkorderID": 41,
    "Product": "Cup",
    "StartDateTime": "2024-10-01 18:49",
    "EndDateTime": "2024-10-02 01:49",
    "Process": "Preparing",
    "Operators": "Operator1, Operator22",
    "Tooling": "Tool13",
    "BatchSize": 105,
    "Quantity": 836
  },
  {
    "WorkorderID": 41,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 20:09",
    "EndDateTime": "2024-10-02 21:09",
    "Process": "Silver Plating",
    "Operators": "Operator32",
    "Tooling": "Tool4, Tool3",
    "BatchSize": 105,
    "Quantity": 836
  },
  {
    "WorkorderID": 41,
    "Product": "Cup",
    "StartDateTime": "2024-10-03 16:20",
    "EndDateTime": "2024-10-03 18:20",
    "Process": "Polishing",
    "Operators": "Operator22",
    "Tooling": "Tool19, Tool16",
    "BatchSize": 105,
    "Quantity": 836
  },
  {
    "WorkorderID": 41,
    "Product": "Cup",
    "StartDateTime": "2024-10-04 10:43",
    "EndDateTime": "2024-10-04 11:43",
    "Process": "Conditioning",
    "Operators": "Operator46, Operator56, Operator79, Operator131, Operator57",
    "Tooling": "Tool4, Tool28",
    "BatchSize": 105,
    "Quantity": 836
  },
  {
    "WorkorderID": 42,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator90, Operator64, Operator130",
    "Tooling": "Tool7, Tool14",
    "BatchSize": 93,
    "Quantity": 1003
  },
  {
    "WorkorderID": 42,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 22:59",
    "EndDateTime": "2024-10-02 06:59",
    "Process": "Preparing",
    "Operators": "Operator6, Operator140",
    "Tooling": "Tool19, Tool11, Tool1",
    "BatchSize": 93,
    "Quantity": 1003
  },
  {
    "WorkorderID": 42,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 02:38",
    "EndDateTime": "2024-10-03 03:38",
    "Process": "Silver Plating",
    "Operators": "Operator56, Operator34, Operator17",
    "Tooling": "Tool25, Tool27, Tool9",
    "BatchSize": 93,
    "Quantity": 1003
  },
  {
    "WorkorderID": 42,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 10:36",
    "EndDateTime": "2024-10-03 18:36",
    "Process": "Polishing",
    "Operators": "Operator94, Operator126, Operator40, Operator29",
    "Tooling": "Tool13",
    "BatchSize": 93,
    "Quantity": 1003
  },
  {
    "WorkorderID": 42,
    "Product": "Mug",
    "StartDateTime": "2024-10-04 15:01",
    "EndDateTime": "2024-10-04 22:01",
    "Process": "Conditioning",
    "Operators": "Operator36, Operator2",
    "Tooling": "Tool29",
    "BatchSize": 93,
    "Quantity": 1003
  },
  {
    "WorkorderID": 43,
    "Product": "Spoon",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator136, Operator30, Operator23",
    "Tooling": "Tool29, Tool1",
    "BatchSize": 91,
    "Quantity": 1448
  },
  {
    "WorkorderID": 43,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 08:19",
    "EndDateTime": "2024-10-01 15:19",
    "Process": "Preparing",
    "Operators": "Operator48, Operator46, Operator14, Operator109, Operator110",
    "Tooling": "Tool22, Tool21, Tool28",
    "BatchSize": 91,
    "Quantity": 1448
  },
  {
    "WorkorderID": 43,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 06:03",
    "EndDateTime": "2024-10-02 13:03",
    "Process": "Silver Plating",
    "Operators": "Operator116, Operator82, Operator88",
    "Tooling": "Tool20, Tool2",
    "BatchSize": 91,
    "Quantity": 1448
  },
  {
    "WorkorderID": 43,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 20:15",
    "EndDateTime": "2024-10-03 02:15",
    "Process": "Polishing",
    "Operators": "Operator143",
    "Tooling": "Tool3, Tool14",
    "BatchSize": 91,
    "Quantity": 1448
  },
  {
    "WorkorderID": 43,
    "Product": "Spoon",
    "StartDateTime": "2024-10-03 17:49",
    "EndDateTime": "2024-10-04 01:49",
    "Process": "Conditioning",
    "Operators": "Operator14",
    "Tooling": "Tool15, Tool4, Tool30",
    "BatchSize": 91,
    "Quantity": 1448
  },
  {
    "WorkorderID": 44,
    "Product": "Saucepan",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator8, Operator116, Operator26, Operator19",
    "Tooling": "Tool15, Tool4",
    "BatchSize": 116,
    "Quantity": 614
  },
  {
    "WorkorderID": 44,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-01 05:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Preparing",
    "Operators": "Operator36, Operator34",
    "Tooling": "Tool12, Tool2, Tool17",
    "BatchSize": 116,
    "Quantity": 614
  },
  {
    "WorkorderID": 44,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-01 17:19",
    "EndDateTime": "2024-10-01 21:19",
    "Process": "Silver Plating",
    "Operators": "Operator46, Operator26, Operator1, Operator36, Operator39",
    "Tooling": "Tool20, Tool30",
    "BatchSize": 116,
    "Quantity": 614
  },
  {
    "WorkorderID": 44,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-02 04:58",
    "EndDateTime": "2024-10-02 05:58",
    "Process": "Polishing",
    "Operators": "Operator97, Operator80, Operator46",
    "Tooling": "Tool1, Tool19",
    "BatchSize": 116,
    "Quantity": 614
  },
  {
    "WorkorderID": 44,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-02 12:57",
    "EndDateTime": "2024-10-02 15:57",
    "Process": "Conditioning",
    "Operators": "Operator17",
    "Tooling": "Tool1, Tool22, Tool9",
    "BatchSize": 116,
    "Quantity": 614
  },
  {
    "WorkorderID": 45,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator10, Operator57",
    "Tooling": "Tool10, Tool11, Tool30",
    "BatchSize": 62,
    "Quantity": 1147
  },
  {
    "WorkorderID": 45,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 02:43",
    "EndDateTime": "2024-10-02 08:43",
    "Process": "Preparing",
    "Operators": "Operator112, Operator70, Operator138",
    "Tooling": "Tool26",
    "BatchSize": 62,
    "Quantity": 1147
  },
  {
    "WorkorderID": 45,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 12:58",
    "EndDateTime": "2024-10-02 16:58",
    "Process": "Silver Plating",
    "Operators": "Operator28, Operator103, Operator145, Operator75",
    "Tooling": "Tool13",
    "BatchSize": 62,
    "Quantity": 1147
  },
  {
    "WorkorderID": 45,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 03:42",
    "EndDateTime": "2024-10-03 05:42",
    "Process": "Polishing",
    "Operators": "Operator88",
    "Tooling": "Tool17, Tool13",
    "BatchSize": 62,
    "Quantity": 1147
  },
  {
    "WorkorderID": 45,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 11:03",
    "EndDateTime": "2024-10-03 15:03",
    "Process": "Conditioning",
    "Operators": "Operator30, Operator93, Operator54, Operator39, Operator122",
    "Tooling": "Tool21, Tool12, Tool20",
    "BatchSize": 62,
    "Quantity": 1147
  },
  {
    "WorkorderID": 46,
    "Product": "Tray",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator122, Operator39, Operator119, Operator4, Operator145",
    "Tooling": "Tool11, Tool21, Tool7",
    "BatchSize": 57,
    "Quantity": 1187
  },
  {
    "WorkorderID": 46,
    "Product": "Tray",
    "StartDateTime": "2024-10-01 16:53",
    "EndDateTime": "2024-10-02 00:53",
    "Process": "Preparing",
    "Operators": "Operator144, Operator69, Operator80, Operator118, Operator119",
    "Tooling": "Tool14, Tool2",
    "BatchSize": 57,
    "Quantity": 1187
  },
  {
    "WorkorderID": 46,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 01:37",
    "EndDateTime": "2024-10-02 07:37",
    "Process": "Silver Plating",
    "Operators": "Operator127, Operator102",
    "Tooling": "Tool9, Tool24, Tool23",
    "BatchSize": 57,
    "Quantity": 1187
  },
  {
    "WorkorderID": 46,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 03:20",
    "EndDateTime": "2024-10-03 11:20",
    "Process": "Polishing",
    "Operators": "Operator57, Operator149, Operator22",
    "Tooling": "Tool16",
    "BatchSize": 57,
    "Quantity": 1187
  },
  {
    "WorkorderID": 46,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 22:24",
    "EndDateTime": "2024-10-04 05:24",
    "Process": "Conditioning",
    "Operators": "Operator64, Operator111, Operator97",
    "Tooling": "Tool7, Tool19, Tool23",
    "BatchSize": 57,
    "Quantity": 1187
  },
  {
    "WorkorderID": 47,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator69, Operator140, Operator126, Operator123, Operator50",
    "Tooling": "Tool23",
    "BatchSize": 68,
    "Quantity": 527
  },
  {
    "WorkorderID": 47,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 17:03",
    "EndDateTime": "2024-10-01 21:03",
    "Process": "Preparing",
    "Operators": "Operator136",
    "Tooling": "Tool17, Tool20, Tool21",
    "BatchSize": 68,
    "Quantity": 527
  },
  {
    "WorkorderID": 47,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 17:59",
    "EndDateTime": "2024-10-02 18:59",
    "Process": "Silver Plating",
    "Operators": "Operator34, Operator44, Operator75, Operator38, Operator20",
    "Tooling": "Tool7, Tool26",
    "BatchSize": 68,
    "Quantity": 527
  },
  {
    "WorkorderID": 47,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 13:06",
    "EndDateTime": "2024-10-03 16:06",
    "Process": "Polishing",
    "Operators": "Operator5, Operator53",
    "Tooling": "Tool25, Tool7, Tool23",
    "BatchSize": 68,
    "Quantity": 527
  },
  {
    "WorkorderID": 47,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 23:42",
    "EndDateTime": "2024-10-04 05:42",
    "Process": "Conditioning",
    "Operators": "Operator24, Operator138, Operator132, Operator146, Operator5",
    "Tooling": "Tool25, Tool7, Tool16",
    "BatchSize": 68,
    "Quantity": 527
  },
  {
    "WorkorderID": 48,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator42, Operator115, Operator73",
    "Tooling": "Tool7, Tool9",
    "BatchSize": 54,
    "Quantity": 543
  },
  {
    "WorkorderID": 48,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 05:21",
    "EndDateTime": "2024-10-01 11:21",
    "Process": "Preparing",
    "Operators": "Operator20, Operator126, Operator45",
    "Tooling": "Tool27, Tool5, Tool23",
    "BatchSize": 54,
    "Quantity": 543
  },
  {
    "WorkorderID": 48,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 16:48",
    "EndDateTime": "2024-10-01 18:48",
    "Process": "Silver Plating",
    "Operators": "Operator11, Operator77, Operator114, Operator110",
    "Tooling": "Tool8, Tool23",
    "BatchSize": 54,
    "Quantity": 543
  },
  {
    "WorkorderID": 48,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 10:04",
    "EndDateTime": "2024-10-02 12:04",
    "Process": "Polishing",
    "Operators": "Operator110, Operator16, Operator4",
    "Tooling": "Tool3, Tool7, Tool27",
    "BatchSize": 54,
    "Quantity": 543
  },
  {
    "WorkorderID": 48,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 12:39",
    "EndDateTime": "2024-10-02 19:39",
    "Process": "Conditioning",
    "Operators": "Operator101, Operator143, Operator103",
    "Tooling": "Tool3, Tool16",
    "BatchSize": 54,
    "Quantity": 543
  },
  {
    "WorkorderID": 49,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator9, Operator137",
    "Tooling": "Tool1, Tool28",
    "BatchSize": 138,
    "Quantity": 633
  },
  {
    "WorkorderID": 49,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 08:09",
    "EndDateTime": "2024-10-01 09:09",
    "Process": "Preparing",
    "Operators": "Operator4, Operator139, Operator150, Operator122",
    "Tooling": "Tool19, Tool25, Tool26",
    "BatchSize": 138,
    "Quantity": 633
  },
  {
    "WorkorderID": 49,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 18:09",
    "EndDateTime": "2024-10-02 00:09",
    "Process": "Silver Plating",
    "Operators": "Operator13, Operator126, Operator95, Operator26, Operator41",
    "Tooling": "Tool10",
    "BatchSize": 138,
    "Quantity": 633
  },
  {
    "WorkorderID": 49,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 12:50",
    "EndDateTime": "2024-10-02 20:50",
    "Process": "Polishing",
    "Operators": "Operator113, Operator8, Operator105, Operator70, Operator32",
    "Tooling": "Tool27, Tool4",
    "BatchSize": 138,
    "Quantity": 633
  },
  {
    "WorkorderID": 49,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 07:29",
    "EndDateTime": "2024-10-03 12:29",
    "Process": "Conditioning",
    "Operators": "Operator150, Operator49, Operator147",
    "Tooling": "Tool25",
    "BatchSize": 138,
    "Quantity": 633
  },
  {
    "WorkorderID": 50,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator145, Operator95",
    "Tooling": "Tool8, Tool20",
    "BatchSize": 79,
    "Quantity": 1314
  },
  {
    "WorkorderID": 50,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 13:40",
    "EndDateTime": "2024-10-01 16:40",
    "Process": "Preparing",
    "Operators": "Operator13, Operator88, Operator36, Operator23, Operator10",
    "Tooling": "Tool26, Tool8",
    "BatchSize": 79,
    "Quantity": 1314
  },
  {
    "WorkorderID": 50,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 06:05",
    "EndDateTime": "2024-10-02 08:05",
    "Process": "Silver Plating",
    "Operators": "Operator98, Operator115, Operator118, Operator3",
    "Tooling": "Tool29, Tool10",
    "BatchSize": 79,
    "Quantity": 1314
  },
  {
    "WorkorderID": 50,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 10:10",
    "EndDateTime": "2024-10-02 18:10",
    "Process": "Polishing",
    "Operators": "Operator93, Operator107",
    "Tooling": "Tool18, Tool10",
    "BatchSize": 79,
    "Quantity": 1314
  },
  {
    "WorkorderID": 50,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 20:05",
    "EndDateTime": "2024-10-02 22:05",
    "Process": "Conditioning",
    "Operators": "Operator13, Operator106",
    "Tooling": "Tool5, Tool3, Tool16",
    "BatchSize": 79,
    "Quantity": 1314
  },
  {
    "WorkorderID": 51,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator28, Operator36, Operator46",
    "Tooling": "Tool5, Tool20, Tool21",
    "BatchSize": 119,
    "Quantity": 807
  },
  {
    "WorkorderID": 51,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 18:02",
    "EndDateTime": "2024-10-01 19:02",
    "Process": "Preparing",
    "Operators": "Operator52, Operator80, Operator45",
    "Tooling": "Tool5",
    "BatchSize": 119,
    "Quantity": 807
  },
  {
    "WorkorderID": 51,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 05:58",
    "EndDateTime": "2024-10-02 12:58",
    "Process": "Silver Plating",
    "Operators": "Operator15, Operator53, Operator121",
    "Tooling": "Tool19",
    "BatchSize": 119,
    "Quantity": 807
  },
  {
    "WorkorderID": 51,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 22:33",
    "EndDateTime": "2024-10-03 00:33",
    "Process": "Polishing",
    "Operators": "Operator101, Operator41, Operator132, Operator86",
    "Tooling": "Tool4, Tool9",
    "BatchSize": 119,
    "Quantity": 807
  },
  {
    "WorkorderID": 51,
    "Product": "Knife",
    "StartDateTime": "2024-10-03 07:03",
    "EndDateTime": "2024-10-03 10:03",
    "Process": "Conditioning",
    "Operators": "Operator81, Operator116, Operator138, Operator2, Operator50",
    "Tooling": "Tool29, Tool10, Tool7",
    "BatchSize": 119,
    "Quantity": 807
  },
  {
    "WorkorderID": 52,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator117",
    "Tooling": "Tool4",
    "BatchSize": 60,
    "Quantity": 702
  },
  {
    "WorkorderID": 52,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 09:15",
    "EndDateTime": "2024-10-01 14:15",
    "Process": "Preparing",
    "Operators": "Operator11, Operator19",
    "Tooling": "Tool3, Tool28, Tool6",
    "BatchSize": 60,
    "Quantity": 702
  },
  {
    "WorkorderID": 52,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 23:57",
    "EndDateTime": "2024-10-02 06:57",
    "Process": "Silver Plating",
    "Operators": "Operator54",
    "Tooling": "Tool18",
    "BatchSize": 60,
    "Quantity": 702
  },
  {
    "WorkorderID": 52,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 20:44",
    "EndDateTime": "2024-10-02 22:44",
    "Process": "Polishing",
    "Operators": "Operator76",
    "Tooling": "Tool7",
    "BatchSize": 60,
    "Quantity": 702
  },
  {
    "WorkorderID": 52,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 22:47",
    "EndDateTime": "2024-10-03 04:47",
    "Process": "Conditioning",
    "Operators": "Operator8, Operator49, Operator140",
    "Tooling": "Tool29, Tool22, Tool10",
    "BatchSize": 60,
    "Quantity": 702
  },
  {
    "WorkorderID": 53,
    "Product": "Fork",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator51, Operator98, Operator87, Operator137",
    "Tooling": "Tool1, Tool19",
    "BatchSize": 90,
    "Quantity": 1159
  },
  {
    "WorkorderID": 53,
    "Product": "Fork",
    "StartDateTime": "2024-09-30 23:46",
    "EndDateTime": "2024-10-01 07:46",
    "Process": "Preparing",
    "Operators": "Operator21, Operator95, Operator11, Operator47, Operator76",
    "Tooling": "Tool13",
    "BatchSize": 90,
    "Quantity": 1159
  },
  {
    "WorkorderID": 53,
    "Product": "Fork",
    "StartDateTime": "2024-10-02 02:29",
    "EndDateTime": "2024-10-02 10:29",
    "Process": "Silver Plating",
    "Operators": "Operator51, Operator43",
    "Tooling": "Tool28, Tool26",
    "BatchSize": 90,
    "Quantity": 1159
  },
  {
    "WorkorderID": 53,
    "Product": "Fork",
    "StartDateTime": "2024-10-02 17:18",
    "EndDateTime": "2024-10-02 19:18",
    "Process": "Polishing",
    "Operators": "Operator109, Operator75, Operator129, Operator127, Operator39",
    "Tooling": "Tool30, Tool19",
    "BatchSize": 90,
    "Quantity": 1159
  },
  {
    "WorkorderID": 53,
    "Product": "Fork",
    "StartDateTime": "2024-10-03 17:04",
    "EndDateTime": "2024-10-04 01:04",
    "Process": "Conditioning",
    "Operators": "Operator103, Operator5, Operator7, Operator87, Operator20",
    "Tooling": "Tool2, Tool8",
    "BatchSize": 90,
    "Quantity": 1159
  },
  {
    "WorkorderID": 54,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator38, Operator76, Operator142, Operator121",
    "Tooling": "Tool10, Tool4, Tool2",
    "BatchSize": 63,
    "Quantity": 812
  },
  {
    "WorkorderID": 54,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 04:48",
    "EndDateTime": "2024-10-01 09:48",
    "Process": "Preparing",
    "Operators": "Operator127, Operator68, Operator1, Operator120, Operator62",
    "Tooling": "Tool24, Tool3",
    "BatchSize": 63,
    "Quantity": 812
  },
  {
    "WorkorderID": 54,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 20:40",
    "EndDateTime": "2024-10-02 04:40",
    "Process": "Silver Plating",
    "Operators": "Operator102, Operator11, Operator17",
    "Tooling": "Tool29, Tool21, Tool3",
    "BatchSize": 63,
    "Quantity": 812
  },
  {
    "WorkorderID": 54,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 20:28",
    "EndDateTime": "2024-10-03 03:28",
    "Process": "Polishing",
    "Operators": "Operator107, Operator52",
    "Tooling": "Tool16, Tool25, Tool5",
    "BatchSize": 63,
    "Quantity": 812
  },
  {
    "WorkorderID": 54,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 09:10",
    "EndDateTime": "2024-10-03 13:10",
    "Process": "Conditioning",
    "Operators": "Operator147, Operator114, Operator130",
    "Tooling": "Tool17",
    "BatchSize": 63,
    "Quantity": 812
  },
  {
    "WorkorderID": 55,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator44",
    "Tooling": "Tool12",
    "BatchSize": 103,
    "Quantity": 1357
  },
  {
    "WorkorderID": 55,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 03:30",
    "EndDateTime": "2024-10-01 04:30",
    "Process": "Preparing",
    "Operators": "Operator26, Operator50",
    "Tooling": "Tool18, Tool16",
    "BatchSize": 103,
    "Quantity": 1357
  },
  {
    "WorkorderID": 55,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 19:34",
    "EndDateTime": "2024-10-01 22:34",
    "Process": "Silver Plating",
    "Operators": "Operator111",
    "Tooling": "Tool9, Tool11",
    "BatchSize": 103,
    "Quantity": 1357
  },
  {
    "WorkorderID": 55,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 20:24",
    "EndDateTime": "2024-10-03 01:24",
    "Process": "Polishing",
    "Operators": "Operator133, Operator29",
    "Tooling": "Tool9, Tool11, Tool17",
    "BatchSize": 103,
    "Quantity": 1357
  },
  {
    "WorkorderID": 55,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 08:43",
    "EndDateTime": "2024-10-03 14:43",
    "Process": "Conditioning",
    "Operators": "Operator14, Operator102",
    "Tooling": "Tool4",
    "BatchSize": 103,
    "Quantity": 1357
  },
  {
    "WorkorderID": 56,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator26, Operator142",
    "Tooling": "Tool23, Tool10, Tool11",
    "BatchSize": 63,
    "Quantity": 1268
  },
  {
    "WorkorderID": 56,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 18:55",
    "EndDateTime": "2024-10-01 23:55",
    "Process": "Preparing",
    "Operators": "Operator66, Operator86, Operator38, Operator43, Operator27",
    "Tooling": "Tool15, Tool4, Tool9",
    "BatchSize": 63,
    "Quantity": 1268
  },
  {
    "WorkorderID": 56,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 02:09",
    "EndDateTime": "2024-10-02 05:09",
    "Process": "Silver Plating",
    "Operators": "Operator127",
    "Tooling": "Tool25",
    "BatchSize": 63,
    "Quantity": 1268
  },
  {
    "WorkorderID": 56,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 10:07",
    "EndDateTime": "2024-10-02 14:07",
    "Process": "Polishing",
    "Operators": "Operator35, Operator83, Operator126, Operator53, Operator97",
    "Tooling": "Tool12, Tool30, Tool25",
    "BatchSize": 63,
    "Quantity": 1268
  },
  {
    "WorkorderID": 56,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 00:51",
    "EndDateTime": "2024-10-03 03:51",
    "Process": "Conditioning",
    "Operators": "Operator137",
    "Tooling": "Tool22",
    "BatchSize": 63,
    "Quantity": 1268
  },
  {
    "WorkorderID": 57,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator19, Operator146",
    "Tooling": "Tool22",
    "BatchSize": 148,
    "Quantity": 1036
  },
  {
    "WorkorderID": 57,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 05:04",
    "EndDateTime": "2024-10-01 07:04",
    "Process": "Preparing",
    "Operators": "Operator15",
    "Tooling": "Tool8",
    "BatchSize": 148,
    "Quantity": 1036
  },
  {
    "WorkorderID": 57,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 12:10",
    "EndDateTime": "2024-10-01 19:10",
    "Process": "Silver Plating",
    "Operators": "Operator15, Operator47, Operator8",
    "Tooling": "Tool1, Tool8",
    "BatchSize": 148,
    "Quantity": 1036
  },
  {
    "WorkorderID": 57,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 19:58",
    "EndDateTime": "2024-10-01 22:58",
    "Process": "Polishing",
    "Operators": "Operator99, Operator56, Operator135",
    "Tooling": "Tool26, Tool10",
    "BatchSize": 148,
    "Quantity": 1036
  },
  {
    "WorkorderID": 57,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 09:09",
    "EndDateTime": "2024-10-02 17:09",
    "Process": "Conditioning",
    "Operators": "Operator4, Operator99, Operator56, Operator138",
    "Tooling": "Tool22, Tool16, Tool23",
    "BatchSize": 148,
    "Quantity": 1036
  },
  {
    "WorkorderID": 58,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator109, Operator21, Operator32, Operator36, Operator72",
    "Tooling": "Tool29, Tool26",
    "BatchSize": 97,
    "Quantity": 1056
  },
  {
    "WorkorderID": 58,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 06:15",
    "EndDateTime": "2024-10-01 07:15",
    "Process": "Preparing",
    "Operators": "Operator56, Operator8, Operator3, Operator91, Operator136",
    "Tooling": "Tool20, Tool14",
    "BatchSize": 97,
    "Quantity": 1056
  },
  {
    "WorkorderID": 58,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 09:28",
    "EndDateTime": "2024-10-01 14:28",
    "Process": "Silver Plating",
    "Operators": "Operator16",
    "Tooling": "Tool20, Tool11, Tool29",
    "BatchSize": 97,
    "Quantity": 1056
  },
  {
    "WorkorderID": 58,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 14:41",
    "EndDateTime": "2024-10-01 17:41",
    "Process": "Polishing",
    "Operators": "Operator16, Operator13",
    "Tooling": "Tool24, Tool26",
    "BatchSize": 97,
    "Quantity": 1056
  },
  {
    "WorkorderID": 58,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 06:22",
    "EndDateTime": "2024-10-02 13:22",
    "Process": "Conditioning",
    "Operators": "Operator17, Operator36, Operator142",
    "Tooling": "Tool21, Tool24",
    "BatchSize": 97,
    "Quantity": 1056
  },
  {
    "WorkorderID": 59,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator135",
    "Tooling": "Tool20, Tool4, Tool28",
    "BatchSize": 112,
    "Quantity": 872
  },
  {
    "WorkorderID": 59,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 16:14",
    "EndDateTime": "2024-10-01 17:14",
    "Process": "Preparing",
    "Operators": "Operator35, Operator8, Operator38",
    "Tooling": "Tool15, Tool20",
    "BatchSize": 112,
    "Quantity": 872
  },
  {
    "WorkorderID": 59,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 05:50",
    "EndDateTime": "2024-10-02 06:50",
    "Process": "Silver Plating",
    "Operators": "Operator35, Operator16",
    "Tooling": "Tool20, Tool4",
    "BatchSize": 112,
    "Quantity": 872
  },
  {
    "WorkorderID": 59,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 01:55",
    "EndDateTime": "2024-10-03 09:55",
    "Process": "Polishing",
    "Operators": "Operator125",
    "Tooling": "Tool8, Tool28",
    "BatchSize": 112,
    "Quantity": 872
  },
  {
    "WorkorderID": 59,
    "Product": "Bottle",
    "StartDateTime": "2024-10-04 02:08",
    "EndDateTime": "2024-10-04 04:08",
    "Process": "Conditioning",
    "Operators": "Operator82, Operator141, Operator31, Operator119",
    "Tooling": "Tool20, Tool4",
    "BatchSize": 112,
    "Quantity": 872
  },
  {
    "WorkorderID": 60,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator87, Operator107, Operator126, Operator72",
    "Tooling": "Tool5",
    "BatchSize": 117,
    "Quantity": 1137
  },
  {
    "WorkorderID": 60,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 03:57",
    "EndDateTime": "2024-10-02 10:57",
    "Process": "Preparing",
    "Operators": "Operator73, Operator28, Operator100",
    "Tooling": "Tool6, Tool8, Tool24",
    "BatchSize": 117,
    "Quantity": 1137
  },
  {
    "WorkorderID": 60,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 14:16",
    "EndDateTime": "2024-10-02 15:16",
    "Process": "Silver Plating",
    "Operators": "Operator19, Operator144",
    "Tooling": "Tool12",
    "BatchSize": 117,
    "Quantity": 1137
  },
  {
    "WorkorderID": 60,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 16:44",
    "EndDateTime": "2024-10-02 23:44",
    "Process": "Polishing",
    "Operators": "Operator118, Operator31, Operator93, Operator39, Operator112",
    "Tooling": "Tool15",
    "BatchSize": 117,
    "Quantity": 1137
  },
  {
    "WorkorderID": 60,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 20:12",
    "EndDateTime": "2024-10-03 21:12",
    "Process": "Conditioning",
    "Operators": "Operator137",
    "Tooling": "Tool28",
    "BatchSize": 117,
    "Quantity": 1137
  },
  {
    "WorkorderID": 61,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator8, Operator117",
    "Tooling": "Tool28",
    "BatchSize": 106,
    "Quantity": 1058
  },
  {
    "WorkorderID": 61,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 22:39",
    "EndDateTime": "2024-10-02 06:39",
    "Process": "Preparing",
    "Operators": "Operator8, Operator14, Operator82, Operator126, Operator1",
    "Tooling": "Tool22, Tool23, Tool20",
    "BatchSize": 106,
    "Quantity": 1058
  },
  {
    "WorkorderID": 61,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 11:17",
    "EndDateTime": "2024-10-02 14:17",
    "Process": "Silver Plating",
    "Operators": "Operator111, Operator143, Operator123, Operator56, Operator133",
    "Tooling": "Tool5, Tool11",
    "BatchSize": 106,
    "Quantity": 1058
  },
  {
    "WorkorderID": 61,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 15:37",
    "EndDateTime": "2024-10-02 22:37",
    "Process": "Polishing",
    "Operators": "Operator66, Operator140, Operator69, Operator63, Operator67",
    "Tooling": "Tool3",
    "BatchSize": 106,
    "Quantity": 1058
  },
  {
    "WorkorderID": 61,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 19:39",
    "EndDateTime": "2024-10-03 22:39",
    "Process": "Conditioning",
    "Operators": "Operator40",
    "Tooling": "Tool4, Tool23",
    "BatchSize": 106,
    "Quantity": 1058
  },
  {
    "WorkorderID": 62,
    "Product": "Spoon",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator37, Operator17",
    "Tooling": "Tool29, Tool12, Tool5",
    "BatchSize": 74,
    "Quantity": 776
  },
  {
    "WorkorderID": 62,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 13:13",
    "EndDateTime": "2024-10-01 18:13",
    "Process": "Preparing",
    "Operators": "Operator106, Operator100",
    "Tooling": "Tool24, Tool25",
    "BatchSize": 74,
    "Quantity": 776
  },
  {
    "WorkorderID": 62,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 20:22",
    "EndDateTime": "2024-10-02 01:22",
    "Process": "Silver Plating",
    "Operators": "Operator116, Operator43",
    "Tooling": "Tool4",
    "BatchSize": 74,
    "Quantity": 776
  },
  {
    "WorkorderID": 62,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 20:49",
    "EndDateTime": "2024-10-02 23:49",
    "Process": "Polishing",
    "Operators": "Operator105, Operator13, Operator89",
    "Tooling": "Tool24, Tool20, Tool15",
    "BatchSize": 74,
    "Quantity": 776
  },
  {
    "WorkorderID": 62,
    "Product": "Spoon",
    "StartDateTime": "2024-10-03 03:55",
    "EndDateTime": "2024-10-03 10:55",
    "Process": "Conditioning",
    "Operators": "Operator98, Operator36, Operator31, Operator121, Operator62",
    "Tooling": "Tool24",
    "BatchSize": 74,
    "Quantity": 776
  },
  {
    "WorkorderID": 63,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator138, Operator27, Operator21, Operator109",
    "Tooling": "Tool22, Tool13, Tool10",
    "BatchSize": 123,
    "Quantity": 556
  },
  {
    "WorkorderID": 63,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 11:26",
    "EndDateTime": "2024-10-01 12:26",
    "Process": "Preparing",
    "Operators": "Operator123, Operator147, Operator32, Operator144",
    "Tooling": "Tool21, Tool11",
    "BatchSize": 123,
    "Quantity": 556
  },
  {
    "WorkorderID": 63,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 05:24",
    "EndDateTime": "2024-10-02 13:24",
    "Process": "Silver Plating",
    "Operators": "Operator32, Operator30, Operator109",
    "Tooling": "Tool22, Tool18",
    "BatchSize": 123,
    "Quantity": 556
  },
  {
    "WorkorderID": 63,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 08:48",
    "EndDateTime": "2024-10-03 15:48",
    "Process": "Polishing",
    "Operators": "Operator105, Operator113, Operator117, Operator141",
    "Tooling": "Tool3, Tool18, Tool5",
    "BatchSize": 123,
    "Quantity": 556
  },
  {
    "WorkorderID": 63,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-04 00:35",
    "EndDateTime": "2024-10-04 08:35",
    "Process": "Conditioning",
    "Operators": "Operator59, Operator66, Operator20, Operator56, Operator54",
    "Tooling": "Tool6",
    "BatchSize": 123,
    "Quantity": 556
  },
  {
    "WorkorderID": 64,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator121, Operator76, Operator150",
    "Tooling": "Tool21",
    "BatchSize": 132,
    "Quantity": 749
  },
  {
    "WorkorderID": 64,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 23:32",
    "EndDateTime": "2024-10-02 04:32",
    "Process": "Preparing",
    "Operators": "Operator126, Operator113, Operator71",
    "Tooling": "Tool5, Tool17",
    "BatchSize": 132,
    "Quantity": 749
  },
  {
    "WorkorderID": 64,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 06:06",
    "EndDateTime": "2024-10-02 08:06",
    "Process": "Silver Plating",
    "Operators": "Operator48, Operator24, Operator28",
    "Tooling": "Tool4, Tool10",
    "BatchSize": 132,
    "Quantity": 749
  },
  {
    "WorkorderID": 64,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 01:10",
    "EndDateTime": "2024-10-03 05:10",
    "Process": "Polishing",
    "Operators": "Operator141, Operator22",
    "Tooling": "Tool1, Tool22, Tool5",
    "BatchSize": 132,
    "Quantity": 749
  },
  {
    "WorkorderID": 64,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-04 02:57",
    "EndDateTime": "2024-10-04 10:57",
    "Process": "Conditioning",
    "Operators": "Operator29, Operator103, Operator65",
    "Tooling": "Tool12",
    "BatchSize": 132,
    "Quantity": 749
  },
  {
    "WorkorderID": 65,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator143, Operator125, Operator100",
    "Tooling": "Tool7",
    "BatchSize": 74,
    "Quantity": 777
  },
  {
    "WorkorderID": 65,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 22:00",
    "EndDateTime": "2024-10-02 04:00",
    "Process": "Preparing",
    "Operators": "Operator19, Operator63",
    "Tooling": "Tool8",
    "BatchSize": 74,
    "Quantity": 777
  },
  {
    "WorkorderID": 65,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 15:55",
    "EndDateTime": "2024-10-02 20:55",
    "Process": "Silver Plating",
    "Operators": "Operator46, Operator60, Operator148, Operator111",
    "Tooling": "Tool18",
    "BatchSize": 74,
    "Quantity": 777
  },
  {
    "WorkorderID": 65,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 01:13",
    "EndDateTime": "2024-10-03 06:13",
    "Process": "Polishing",
    "Operators": "Operator73, Operator113",
    "Tooling": "Tool11",
    "BatchSize": 74,
    "Quantity": 777
  },
  {
    "WorkorderID": 65,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 13:49",
    "EndDateTime": "2024-10-03 19:49",
    "Process": "Conditioning",
    "Operators": "Operator100, Operator5, Operator69, Operator57",
    "Tooling": "Tool7, Tool28",
    "BatchSize": 74,
    "Quantity": 777
  },
  {
    "WorkorderID": 66,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator37",
    "Tooling": "Tool12",
    "BatchSize": 87,
    "Quantity": 773
  },
  {
    "WorkorderID": 66,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 02:23",
    "EndDateTime": "2024-10-02 10:23",
    "Process": "Preparing",
    "Operators": "Operator60, Operator96, Operator76, Operator65, Operator34",
    "Tooling": "Tool17, Tool1",
    "BatchSize": 87,
    "Quantity": 773
  },
  {
    "WorkorderID": 66,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 21:46",
    "EndDateTime": "2024-10-03 01:46",
    "Process": "Silver Plating",
    "Operators": "Operator45, Operator127, Operator63, Operator135, Operator129",
    "Tooling": "Tool25, Tool17",
    "BatchSize": 87,
    "Quantity": 773
  },
  {
    "WorkorderID": 66,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 09:06",
    "EndDateTime": "2024-10-03 11:06",
    "Process": "Polishing",
    "Operators": "Operator117, Operator55, Operator24",
    "Tooling": "Tool21",
    "BatchSize": 87,
    "Quantity": 773
  },
  {
    "WorkorderID": 66,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 21:00",
    "EndDateTime": "2024-10-04 00:00",
    "Process": "Conditioning",
    "Operators": "Operator75, Operator102, Operator95, Operator84, Operator125",
    "Tooling": "Tool1, Tool23, Tool18",
    "BatchSize": 87,
    "Quantity": 773
  },
  {
    "WorkorderID": 67,
    "Product": "Spoon",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator27, Operator103, Operator144",
    "Tooling": "Tool25",
    "BatchSize": 120,
    "Quantity": 779
  },
  {
    "WorkorderID": 67,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 06:31",
    "EndDateTime": "2024-10-01 12:31",
    "Process": "Preparing",
    "Operators": "Operator27, Operator103, Operator105",
    "Tooling": "Tool13, Tool10, Tool20",
    "BatchSize": 120,
    "Quantity": 779
  },
  {
    "WorkorderID": 67,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 23:54",
    "EndDateTime": "2024-10-02 04:54",
    "Process": "Silver Plating",
    "Operators": "Operator2",
    "Tooling": "Tool19, Tool20, Tool12",
    "BatchSize": 120,
    "Quantity": 779
  },
  {
    "WorkorderID": 67,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 19:54",
    "EndDateTime": "2024-10-03 02:54",
    "Process": "Polishing",
    "Operators": "Operator48",
    "Tooling": "Tool19, Tool24",
    "BatchSize": 120,
    "Quantity": 779
  },
  {
    "WorkorderID": 67,
    "Product": "Spoon",
    "StartDateTime": "2024-10-03 09:02",
    "EndDateTime": "2024-10-03 13:02",
    "Process": "Conditioning",
    "Operators": "Operator89, Operator110, Operator80, Operator120",
    "Tooling": "Tool13",
    "BatchSize": 120,
    "Quantity": 779
  },
  {
    "WorkorderID": 68,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator2, Operator61, Operator146, Operator44, Operator75",
    "Tooling": "Tool6, Tool18",
    "BatchSize": 68,
    "Quantity": 859
  },
  {
    "WorkorderID": 68,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 06:37",
    "EndDateTime": "2024-10-01 09:37",
    "Process": "Preparing",
    "Operators": "Operator71, Operator90, Operator81",
    "Tooling": "Tool16, Tool2, Tool6",
    "BatchSize": 68,
    "Quantity": 859
  },
  {
    "WorkorderID": 68,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 12:56",
    "EndDateTime": "2024-10-01 17:56",
    "Process": "Silver Plating",
    "Operators": "Operator1, Operator124, Operator71, Operator114",
    "Tooling": "Tool28, Tool14",
    "BatchSize": 68,
    "Quantity": 859
  },
  {
    "WorkorderID": 68,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 17:49",
    "EndDateTime": "2024-10-02 19:49",
    "Process": "Polishing",
    "Operators": "Operator50, Operator54, Operator92, Operator12",
    "Tooling": "Tool21",
    "BatchSize": 68,
    "Quantity": 859
  },
  {
    "WorkorderID": 68,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 05:34",
    "EndDateTime": "2024-10-03 08:34",
    "Process": "Conditioning",
    "Operators": "Operator125, Operator99, Operator1, Operator88, Operator12",
    "Tooling": "Tool6, Tool2, Tool15",
    "BatchSize": 68,
    "Quantity": 859
  },
  {
    "WorkorderID": 69,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator96, Operator68, Operator62, Operator72",
    "Tooling": "Tool19, Tool10, Tool29",
    "BatchSize": 141,
    "Quantity": 1184
  },
  {
    "WorkorderID": 69,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 22:13",
    "EndDateTime": "2024-10-02 06:13",
    "Process": "Preparing",
    "Operators": "Operator96, Operator114, Operator121, Operator40",
    "Tooling": "Tool25, Tool17",
    "BatchSize": 141,
    "Quantity": 1184
  },
  {
    "WorkorderID": 69,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 21:56",
    "EndDateTime": "2024-10-02 23:56",
    "Process": "Silver Plating",
    "Operators": "Operator119",
    "Tooling": "Tool6",
    "BatchSize": 141,
    "Quantity": 1184
  },
  {
    "WorkorderID": 69,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 04:30",
    "EndDateTime": "2024-10-03 12:30",
    "Process": "Polishing",
    "Operators": "Operator76",
    "Tooling": "Tool14, Tool27",
    "BatchSize": 141,
    "Quantity": 1184
  },
  {
    "WorkorderID": 69,
    "Product": "Teapot",
    "StartDateTime": "2024-10-04 05:49",
    "EndDateTime": "2024-10-04 13:49",
    "Process": "Conditioning",
    "Operators": "Operator38",
    "Tooling": "Tool28, Tool26, Tool20",
    "BatchSize": 141,
    "Quantity": 1184
  },
  {
    "WorkorderID": 70,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator148, Operator12, Operator35",
    "Tooling": "Tool28",
    "BatchSize": 132,
    "Quantity": 1469
  },
  {
    "WorkorderID": 70,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 21:33",
    "EndDateTime": "2024-10-02 04:33",
    "Process": "Preparing",
    "Operators": "Operator24, Operator100, Operator11",
    "Tooling": "Tool8, Tool25",
    "BatchSize": 132,
    "Quantity": 1469
  },
  {
    "WorkorderID": 70,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 22:23",
    "EndDateTime": "2024-10-03 01:23",
    "Process": "Silver Plating",
    "Operators": "Operator21, Operator96",
    "Tooling": "Tool2, Tool26",
    "BatchSize": 132,
    "Quantity": 1469
  },
  {
    "WorkorderID": 70,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 02:44",
    "EndDateTime": "2024-10-03 04:44",
    "Process": "Polishing",
    "Operators": "Operator146, Operator39",
    "Tooling": "Tool5",
    "BatchSize": 132,
    "Quantity": 1469
  },
  {
    "WorkorderID": 70,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 19:32",
    "EndDateTime": "2024-10-03 20:32",
    "Process": "Conditioning",
    "Operators": "Operator130, Operator45, Operator26",
    "Tooling": "Tool24, Tool19, Tool25",
    "BatchSize": 132,
    "Quantity": 1469
  },
  {
    "WorkorderID": 71,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator27, Operator94, Operator93",
    "Tooling": "Tool21",
    "BatchSize": 138,
    "Quantity": 1109
  },
  {
    "WorkorderID": 71,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 22:39",
    "EndDateTime": "2024-10-02 00:39",
    "Process": "Preparing",
    "Operators": "Operator83, Operator119, Operator66, Operator130",
    "Tooling": "Tool2, Tool25, Tool17",
    "BatchSize": 138,
    "Quantity": 1109
  },
  {
    "WorkorderID": 71,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 13:43",
    "EndDateTime": "2024-10-02 16:43",
    "Process": "Silver Plating",
    "Operators": "Operator131, Operator133",
    "Tooling": "Tool15, Tool20",
    "BatchSize": 138,
    "Quantity": 1109
  },
  {
    "WorkorderID": 71,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 10:57",
    "EndDateTime": "2024-10-03 18:57",
    "Process": "Polishing",
    "Operators": "Operator11, Operator124, Operator131",
    "Tooling": "Tool9, Tool20, Tool2",
    "BatchSize": 138,
    "Quantity": 1109
  },
  {
    "WorkorderID": 71,
    "Product": "Jug",
    "StartDateTime": "2024-10-04 08:12",
    "EndDateTime": "2024-10-04 11:12",
    "Process": "Conditioning",
    "Operators": "Operator127",
    "Tooling": "Tool22, Tool8, Tool12",
    "BatchSize": 138,
    "Quantity": 1109
  },
  {
    "WorkorderID": 72,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator88, Operator5",
    "Tooling": "Tool12",
    "BatchSize": 101,
    "Quantity": 901
  },
  {
    "WorkorderID": 72,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 07:05",
    "EndDateTime": "2024-10-01 09:05",
    "Process": "Preparing",
    "Operators": "Operator142, Operator105",
    "Tooling": "Tool22",
    "BatchSize": 101,
    "Quantity": 901
  },
  {
    "WorkorderID": 72,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 20:00",
    "EndDateTime": "2024-10-01 23:00",
    "Process": "Silver Plating",
    "Operators": "Operator58",
    "Tooling": "Tool16, Tool15, Tool29",
    "BatchSize": 101,
    "Quantity": 901
  },
  {
    "WorkorderID": 72,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 17:55",
    "EndDateTime": "2024-10-03 00:55",
    "Process": "Polishing",
    "Operators": "Operator113, Operator54, Operator84, Operator121",
    "Tooling": "Tool29, Tool3",
    "BatchSize": 101,
    "Quantity": 901
  },
  {
    "WorkorderID": 72,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 22:05",
    "EndDateTime": "2024-10-04 03:05",
    "Process": "Conditioning",
    "Operators": "Operator134, Operator78",
    "Tooling": "Tool30, Tool3",
    "BatchSize": 101,
    "Quantity": 901
  },
  {
    "WorkorderID": 73,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator143, Operator103, Operator149, Operator117, Operator133",
    "Tooling": "Tool14",
    "BatchSize": 114,
    "Quantity": 1405
  },
  {
    "WorkorderID": 73,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 07:11",
    "EndDateTime": "2024-10-01 10:11",
    "Process": "Preparing",
    "Operators": "Operator60, Operator1, Operator36, Operator73, Operator27",
    "Tooling": "Tool22, Tool11, Tool8",
    "BatchSize": 114,
    "Quantity": 1405
  },
  {
    "WorkorderID": 73,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 18:24",
    "EndDateTime": "2024-10-01 22:24",
    "Process": "Silver Plating",
    "Operators": "Operator112, Operator32",
    "Tooling": "Tool6, Tool2, Tool15",
    "BatchSize": 114,
    "Quantity": 1405
  },
  {
    "WorkorderID": 73,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 13:48",
    "EndDateTime": "2024-10-02 20:48",
    "Process": "Polishing",
    "Operators": "Operator134, Operator99, Operator37, Operator5, Operator130",
    "Tooling": "Tool11, Tool17, Tool22",
    "BatchSize": 114,
    "Quantity": 1405
  },
  {
    "WorkorderID": 73,
    "Product": "Knife",
    "StartDateTime": "2024-10-03 18:44",
    "EndDateTime": "2024-10-03 22:44",
    "Process": "Conditioning",
    "Operators": "Operator79",
    "Tooling": "Tool11",
    "BatchSize": 114,
    "Quantity": 1405
  },
  {
    "WorkorderID": 74,
    "Product": "Tray",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator134",
    "Tooling": "Tool7, Tool12",
    "BatchSize": 126,
    "Quantity": 934
  },
  {
    "WorkorderID": 74,
    "Product": "Tray",
    "StartDateTime": "2024-10-01 22:41",
    "EndDateTime": "2024-10-02 00:41",
    "Process": "Preparing",
    "Operators": "Operator40, Operator146, Operator134, Operator83",
    "Tooling": "Tool18",
    "BatchSize": 126,
    "Quantity": 934
  },
  {
    "WorkorderID": 74,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 09:03",
    "EndDateTime": "2024-10-02 15:03",
    "Process": "Silver Plating",
    "Operators": "Operator109, Operator32, Operator68, Operator61",
    "Tooling": "Tool6, Tool11",
    "BatchSize": 126,
    "Quantity": 934
  },
  {
    "WorkorderID": 74,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 05:13",
    "EndDateTime": "2024-10-03 07:13",
    "Process": "Polishing",
    "Operators": "Operator116, Operator109",
    "Tooling": "Tool20, Tool30, Tool29",
    "BatchSize": 126,
    "Quantity": 934
  },
  {
    "WorkorderID": 74,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 07:17",
    "EndDateTime": "2024-10-03 13:17",
    "Process": "Conditioning",
    "Operators": "Operator141, Operator127, Operator101, Operator2, Operator36",
    "Tooling": "Tool19, Tool13",
    "BatchSize": 126,
    "Quantity": 934
  },
  {
    "WorkorderID": 75,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator109, Operator57, Operator129, Operator130, Operator146",
    "Tooling": "Tool11, Tool16",
    "BatchSize": 63,
    "Quantity": 859
  },
  {
    "WorkorderID": 75,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 04:21",
    "EndDateTime": "2024-10-01 08:21",
    "Process": "Preparing",
    "Operators": "Operator40, Operator75, Operator37, Operator131, Operator107",
    "Tooling": "Tool11, Tool15",
    "BatchSize": 63,
    "Quantity": 859
  },
  {
    "WorkorderID": 75,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 20:31",
    "EndDateTime": "2024-10-02 02:31",
    "Process": "Silver Plating",
    "Operators": "Operator72, Operator87, Operator96, Operator148, Operator68",
    "Tooling": "Tool13",
    "BatchSize": 63,
    "Quantity": 859
  },
  {
    "WorkorderID": 75,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 05:42",
    "EndDateTime": "2024-10-02 10:42",
    "Process": "Polishing",
    "Operators": "Operator134, Operator19, Operator120, Operator96",
    "Tooling": "Tool25, Tool2",
    "BatchSize": 63,
    "Quantity": 859
  },
  {
    "WorkorderID": 75,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 19:40",
    "EndDateTime": "2024-10-02 21:40",
    "Process": "Conditioning",
    "Operators": "Operator64, Operator56",
    "Tooling": "Tool8, Tool13, Tool20",
    "BatchSize": 63,
    "Quantity": 859
  },
  {
    "WorkorderID": 76,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator62, Operator16",
    "Tooling": "Tool7",
    "BatchSize": 144,
    "Quantity": 862
  },
  {
    "WorkorderID": 76,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 23:41",
    "EndDateTime": "2024-10-02 01:41",
    "Process": "Preparing",
    "Operators": "Operator95, Operator65, Operator11",
    "Tooling": "Tool8, Tool7, Tool3",
    "BatchSize": 144,
    "Quantity": 862
  },
  {
    "WorkorderID": 76,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 06:08",
    "EndDateTime": "2024-10-02 11:08",
    "Process": "Silver Plating",
    "Operators": "Operator138",
    "Tooling": "Tool1, Tool13",
    "BatchSize": 144,
    "Quantity": 862
  },
  {
    "WorkorderID": 76,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 04:31",
    "EndDateTime": "2024-10-03 08:31",
    "Process": "Polishing",
    "Operators": "Operator22, Operator24, Operator26, Operator131",
    "Tooling": "Tool15, Tool8, Tool11",
    "BatchSize": 144,
    "Quantity": 862
  },
  {
    "WorkorderID": 76,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 10:11",
    "EndDateTime": "2024-10-03 16:11",
    "Process": "Conditioning",
    "Operators": "Operator34, Operator24, Operator62, Operator77",
    "Tooling": "Tool26, Tool25, Tool29",
    "BatchSize": 144,
    "Quantity": 862
  },
  {
    "WorkorderID": 77,
    "Product": "Spoon",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator53, Operator114, Operator115",
    "Tooling": "Tool15",
    "BatchSize": 91,
    "Quantity": 910
  },
  {
    "WorkorderID": 77,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 10:26",
    "EndDateTime": "2024-10-01 12:26",
    "Process": "Preparing",
    "Operators": "Operator46, Operator132, Operator148, Operator121, Operator17",
    "Tooling": "Tool15, Tool27",
    "BatchSize": 91,
    "Quantity": 910
  },
  {
    "WorkorderID": 77,
    "Product": "Spoon",
    "StartDateTime": "2024-10-01 22:39",
    "EndDateTime": "2024-10-02 00:39",
    "Process": "Silver Plating",
    "Operators": "Operator114, Operator38, Operator139, Operator7, Operator59",
    "Tooling": "Tool15, Tool2, Tool22",
    "BatchSize": 91,
    "Quantity": 910
  },
  {
    "WorkorderID": 77,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 10:31",
    "EndDateTime": "2024-10-02 14:31",
    "Process": "Polishing",
    "Operators": "Operator46, Operator116, Operator66, Operator128",
    "Tooling": "Tool26, Tool11",
    "BatchSize": 91,
    "Quantity": 910
  },
  {
    "WorkorderID": 77,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 22:53",
    "EndDateTime": "2024-10-03 01:53",
    "Process": "Conditioning",
    "Operators": "Operator69, Operator88",
    "Tooling": "Tool30",
    "BatchSize": 91,
    "Quantity": 910
  },
  {
    "WorkorderID": 78,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator31",
    "Tooling": "Tool1",
    "BatchSize": 64,
    "Quantity": 1211
  },
  {
    "WorkorderID": 78,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 18:49",
    "EndDateTime": "2024-10-01 20:49",
    "Process": "Preparing",
    "Operators": "Operator14",
    "Tooling": "Tool24, Tool23, Tool30",
    "BatchSize": 64,
    "Quantity": 1211
  },
  {
    "WorkorderID": 78,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 07:43",
    "EndDateTime": "2024-10-02 08:43",
    "Process": "Silver Plating",
    "Operators": "Operator14",
    "Tooling": "Tool27, Tool14",
    "BatchSize": 64,
    "Quantity": 1211
  },
  {
    "WorkorderID": 78,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 00:47",
    "EndDateTime": "2024-10-03 05:47",
    "Process": "Polishing",
    "Operators": "Operator1, Operator86, Operator115, Operator61",
    "Tooling": "Tool18, Tool14",
    "BatchSize": 64,
    "Quantity": 1211
  },
  {
    "WorkorderID": 78,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 06:37",
    "EndDateTime": "2024-10-03 08:37",
    "Process": "Conditioning",
    "Operators": "Operator10, Operator86, Operator22, Operator107, Operator66",
    "Tooling": "Tool10, Tool30",
    "BatchSize": 64,
    "Quantity": 1211
  },
  {
    "WorkorderID": 79,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator120",
    "Tooling": "Tool5, Tool10, Tool16",
    "BatchSize": 67,
    "Quantity": 1415
  },
  {
    "WorkorderID": 79,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 12:41",
    "EndDateTime": "2024-10-01 16:41",
    "Process": "Preparing",
    "Operators": "Operator5, Operator56",
    "Tooling": "Tool16",
    "BatchSize": 67,
    "Quantity": 1415
  },
  {
    "WorkorderID": 79,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 10:15",
    "EndDateTime": "2024-10-02 16:15",
    "Process": "Silver Plating",
    "Operators": "Operator11, Operator91, Operator96, Operator65, Operator111",
    "Tooling": "Tool20, Tool28",
    "BatchSize": 67,
    "Quantity": 1415
  },
  {
    "WorkorderID": 79,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 00:47",
    "EndDateTime": "2024-10-03 05:47",
    "Process": "Polishing",
    "Operators": "Operator124, Operator25, Operator143",
    "Tooling": "Tool18, Tool22",
    "BatchSize": 67,
    "Quantity": 1415
  },
  {
    "WorkorderID": 79,
    "Product": "Teapot",
    "StartDateTime": "2024-10-04 02:11",
    "EndDateTime": "2024-10-04 09:11",
    "Process": "Conditioning",
    "Operators": "Operator64",
    "Tooling": "Tool18",
    "BatchSize": 67,
    "Quantity": 1415
  },
  {
    "WorkorderID": 80,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator44, Operator25",
    "Tooling": "Tool2, Tool28",
    "BatchSize": 147,
    "Quantity": 559
  },
  {
    "WorkorderID": 80,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 08:35",
    "EndDateTime": "2024-10-01 12:35",
    "Process": "Preparing",
    "Operators": "Operator16",
    "Tooling": "Tool26, Tool21, Tool24",
    "BatchSize": 147,
    "Quantity": 559
  },
  {
    "WorkorderID": 80,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 05:37",
    "EndDateTime": "2024-10-02 10:37",
    "Process": "Silver Plating",
    "Operators": "Operator16, Operator51",
    "Tooling": "Tool26",
    "BatchSize": 147,
    "Quantity": 559
  },
  {
    "WorkorderID": 80,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 17:03",
    "EndDateTime": "2024-10-02 22:03",
    "Process": "Polishing",
    "Operators": "Operator39",
    "Tooling": "Tool17, Tool2",
    "BatchSize": 147,
    "Quantity": 559
  },
  {
    "WorkorderID": 80,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 12:10",
    "EndDateTime": "2024-10-03 13:10",
    "Process": "Conditioning",
    "Operators": "Operator122, Operator57",
    "Tooling": "Tool17",
    "BatchSize": 147,
    "Quantity": 559
  },
  {
    "WorkorderID": 81,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator47, Operator126",
    "Tooling": "Tool16, Tool13",
    "BatchSize": 62,
    "Quantity": 1236
  },
  {
    "WorkorderID": 81,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 04:56",
    "EndDateTime": "2024-10-02 06:56",
    "Process": "Preparing",
    "Operators": "Operator85, Operator103",
    "Tooling": "Tool27, Tool13, Tool29",
    "BatchSize": 62,
    "Quantity": 1236
  },
  {
    "WorkorderID": 81,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 23:51",
    "EndDateTime": "2024-10-03 00:51",
    "Process": "Silver Plating",
    "Operators": "Operator6, Operator34, Operator42, Operator102, Operator37",
    "Tooling": "Tool24, Tool11, Tool3",
    "BatchSize": 62,
    "Quantity": 1236
  },
  {
    "WorkorderID": 81,
    "Product": "Knife",
    "StartDateTime": "2024-10-03 01:16",
    "EndDateTime": "2024-10-03 09:16",
    "Process": "Polishing",
    "Operators": "Operator88, Operator42, Operator58",
    "Tooling": "Tool21",
    "BatchSize": 62,
    "Quantity": 1236
  },
  {
    "WorkorderID": 81,
    "Product": "Knife",
    "StartDateTime": "2024-10-04 07:51",
    "EndDateTime": "2024-10-04 10:51",
    "Process": "Conditioning",
    "Operators": "Operator132, Operator87",
    "Tooling": "Tool5",
    "BatchSize": 62,
    "Quantity": 1236
  },
  {
    "WorkorderID": 82,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator47, Operator104, Operator97, Operator22",
    "Tooling": "Tool19, Tool24, Tool14",
    "BatchSize": 108,
    "Quantity": 1480
  },
  {
    "WorkorderID": 82,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 21:18",
    "EndDateTime": "2024-10-01 22:18",
    "Process": "Preparing",
    "Operators": "Operator120, Operator135",
    "Tooling": "Tool10, Tool2",
    "BatchSize": 108,
    "Quantity": 1480
  },
  {
    "WorkorderID": 82,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 15:24",
    "EndDateTime": "2024-10-02 19:24",
    "Process": "Silver Plating",
    "Operators": "Operator8, Operator150, Operator38, Operator35, Operator71",
    "Tooling": "Tool21, Tool8, Tool25",
    "BatchSize": 108,
    "Quantity": 1480
  },
  {
    "WorkorderID": 82,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 21:26",
    "EndDateTime": "2024-10-03 05:26",
    "Process": "Polishing",
    "Operators": "Operator66",
    "Tooling": "Tool22",
    "BatchSize": 108,
    "Quantity": 1480
  },
  {
    "WorkorderID": 82,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 12:41",
    "EndDateTime": "2024-10-03 18:41",
    "Process": "Conditioning",
    "Operators": "Operator14",
    "Tooling": "Tool8",
    "BatchSize": 108,
    "Quantity": 1480
  },
  {
    "WorkorderID": 83,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator130, Operator53, Operator145, Operator31, Operator127",
    "Tooling": "Tool14",
    "BatchSize": 102,
    "Quantity": 726
  },
  {
    "WorkorderID": 83,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 10:54",
    "EndDateTime": "2024-10-01 15:54",
    "Process": "Preparing",
    "Operators": "Operator142, Operator101, Operator83",
    "Tooling": "Tool21, Tool28, Tool7",
    "BatchSize": 102,
    "Quantity": 726
  },
  {
    "WorkorderID": 83,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 20:29",
    "EndDateTime": "2024-10-02 04:29",
    "Process": "Silver Plating",
    "Operators": "Operator86",
    "Tooling": "Tool2",
    "BatchSize": 102,
    "Quantity": 726
  },
  {
    "WorkorderID": 83,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 22:43",
    "EndDateTime": "2024-10-03 06:43",
    "Process": "Polishing",
    "Operators": "Operator134, Operator14, Operator86",
    "Tooling": "Tool14, Tool10",
    "BatchSize": 102,
    "Quantity": 726
  },
  {
    "WorkorderID": 83,
    "Product": "Bottle",
    "StartDateTime": "2024-10-04 02:49",
    "EndDateTime": "2024-10-04 04:49",
    "Process": "Conditioning",
    "Operators": "Operator125, Operator107",
    "Tooling": "Tool6",
    "BatchSize": 102,
    "Quantity": 726
  },
  {
    "WorkorderID": 84,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator30, Operator114, Operator125",
    "Tooling": "Tool7",
    "BatchSize": 50,
    "Quantity": 689
  },
  {
    "WorkorderID": 84,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 08:06",
    "EndDateTime": "2024-10-01 15:06",
    "Process": "Preparing",
    "Operators": "Operator141",
    "Tooling": "Tool18, Tool7, Tool13",
    "BatchSize": 50,
    "Quantity": 689
  },
  {
    "WorkorderID": 84,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 17:58",
    "EndDateTime": "2024-10-01 23:58",
    "Process": "Silver Plating",
    "Operators": "Operator136, Operator59",
    "Tooling": "Tool25",
    "BatchSize": 50,
    "Quantity": 689
  },
  {
    "WorkorderID": 84,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 09:54",
    "EndDateTime": "2024-10-02 10:54",
    "Process": "Polishing",
    "Operators": "Operator2, Operator135, Operator68",
    "Tooling": "Tool11",
    "BatchSize": 50,
    "Quantity": 689
  },
  {
    "WorkorderID": 84,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 01:06",
    "EndDateTime": "2024-10-03 06:06",
    "Process": "Conditioning",
    "Operators": "Operator43, Operator48, Operator88",
    "Tooling": "Tool24, Tool13, Tool20",
    "BatchSize": 50,
    "Quantity": 689
  },
  {
    "WorkorderID": 85,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator84, Operator129, Operator2, Operator77",
    "Tooling": "Tool19, Tool25",
    "BatchSize": 128,
    "Quantity": 509
  },
  {
    "WorkorderID": 85,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 15:10",
    "EndDateTime": "2024-10-01 23:10",
    "Process": "Preparing",
    "Operators": "Operator18, Operator44, Operator8",
    "Tooling": "Tool3, Tool21",
    "BatchSize": 128,
    "Quantity": 509
  },
  {
    "WorkorderID": 85,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 05:52",
    "EndDateTime": "2024-10-02 12:52",
    "Process": "Silver Plating",
    "Operators": "Operator9, Operator146, Operator4, Operator73, Operator135",
    "Tooling": "Tool5, Tool17",
    "BatchSize": 128,
    "Quantity": 509
  },
  {
    "WorkorderID": 85,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 00:51",
    "EndDateTime": "2024-10-03 08:51",
    "Process": "Polishing",
    "Operators": "Operator32",
    "Tooling": "Tool2, Tool18",
    "BatchSize": 128,
    "Quantity": 509
  },
  {
    "WorkorderID": 85,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 13:33",
    "EndDateTime": "2024-10-03 19:33",
    "Process": "Conditioning",
    "Operators": "Operator97, Operator89, Operator29, Operator120, Operator121",
    "Tooling": "Tool14, Tool30",
    "BatchSize": 128,
    "Quantity": 509
  },
  {
    "WorkorderID": 86,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator77, Operator41",
    "Tooling": "Tool8, Tool18, Tool24",
    "BatchSize": 126,
    "Quantity": 722
  },
  {
    "WorkorderID": 86,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 06:09",
    "EndDateTime": "2024-10-01 12:09",
    "Process": "Preparing",
    "Operators": "Operator48",
    "Tooling": "Tool10",
    "BatchSize": 126,
    "Quantity": 722
  },
  {
    "WorkorderID": 86,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 00:40",
    "EndDateTime": "2024-10-02 05:40",
    "Process": "Silver Plating",
    "Operators": "Operator120, Operator15",
    "Tooling": "Tool10",
    "BatchSize": 126,
    "Quantity": 722
  },
  {
    "WorkorderID": 86,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 11:43",
    "EndDateTime": "2024-10-02 18:43",
    "Process": "Polishing",
    "Operators": "Operator131, Operator145",
    "Tooling": "Tool17",
    "BatchSize": 126,
    "Quantity": 722
  },
  {
    "WorkorderID": 86,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 14:26",
    "EndDateTime": "2024-10-03 15:26",
    "Process": "Conditioning",
    "Operators": "Operator44, Operator47, Operator30, Operator125",
    "Tooling": "Tool11, Tool17, Tool20",
    "BatchSize": 126,
    "Quantity": 722
  },
  {
    "WorkorderID": 87,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator23, Operator126, Operator79, Operator36",
    "Tooling": "Tool11, Tool27",
    "BatchSize": 79,
    "Quantity": 748
  },
  {
    "WorkorderID": 87,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 20:15",
    "EndDateTime": "2024-10-02 00:15",
    "Process": "Preparing",
    "Operators": "Operator149, Operator84, Operator43, Operator110",
    "Tooling": "Tool26, Tool9, Tool5",
    "BatchSize": 79,
    "Quantity": 748
  },
  {
    "WorkorderID": 87,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 20:24",
    "EndDateTime": "2024-10-02 21:24",
    "Process": "Silver Plating",
    "Operators": "Operator148, Operator87, Operator137",
    "Tooling": "Tool21",
    "BatchSize": 79,
    "Quantity": 748
  },
  {
    "WorkorderID": 87,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 00:25",
    "EndDateTime": "2024-10-03 01:25",
    "Process": "Polishing",
    "Operators": "Operator125, Operator124, Operator120, Operator136",
    "Tooling": "Tool14, Tool2",
    "BatchSize": 79,
    "Quantity": 748
  },
  {
    "WorkorderID": 87,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 03:15",
    "EndDateTime": "2024-10-03 11:15",
    "Process": "Conditioning",
    "Operators": "Operator146, Operator142, Operator59",
    "Tooling": "Tool12, Tool15, Tool6",
    "BatchSize": 79,
    "Quantity": 748
  },
  {
    "WorkorderID": 88,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator99",
    "Tooling": "Tool15, Tool6",
    "BatchSize": 127,
    "Quantity": 1271
  },
  {
    "WorkorderID": 88,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 21:13",
    "EndDateTime": "2024-10-02 01:13",
    "Process": "Preparing",
    "Operators": "Operator145, Operator12, Operator86",
    "Tooling": "Tool30",
    "BatchSize": 127,
    "Quantity": 1271
  },
  {
    "WorkorderID": 88,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 15:26",
    "EndDateTime": "2024-10-02 23:26",
    "Process": "Silver Plating",
    "Operators": "Operator132, Operator89, Operator34, Operator105",
    "Tooling": "Tool11, Tool14",
    "BatchSize": 127,
    "Quantity": 1271
  },
  {
    "WorkorderID": 88,
    "Product": "Coaster",
    "StartDateTime": "2024-10-02 23:40",
    "EndDateTime": "2024-10-03 01:40",
    "Process": "Polishing",
    "Operators": "Operator79",
    "Tooling": "Tool4",
    "BatchSize": 127,
    "Quantity": 1271
  },
  {
    "WorkorderID": 88,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 02:10",
    "EndDateTime": "2024-10-03 07:10",
    "Process": "Conditioning",
    "Operators": "Operator44, Operator81, Operator148, Operator137",
    "Tooling": "Tool2, Tool17, Tool24",
    "BatchSize": 127,
    "Quantity": 1271
  },
  {
    "WorkorderID": 89,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator128, Operator42, Operator109, Operator113, Operator134",
    "Tooling": "Tool14, Tool24",
    "BatchSize": 78,
    "Quantity": 849
  },
  {
    "WorkorderID": 89,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 11:45",
    "EndDateTime": "2024-10-01 12:45",
    "Process": "Preparing",
    "Operators": "Operator30, Operator70, Operator110, Operator101, Operator4",
    "Tooling": "Tool9",
    "BatchSize": 78,
    "Quantity": 849
  },
  {
    "WorkorderID": 89,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 14:18",
    "EndDateTime": "2024-10-01 20:18",
    "Process": "Silver Plating",
    "Operators": "Operator102",
    "Tooling": "Tool5, Tool2",
    "BatchSize": 78,
    "Quantity": 849
  },
  {
    "WorkorderID": 89,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 14:45",
    "EndDateTime": "2024-10-02 22:45",
    "Process": "Polishing",
    "Operators": "Operator35, Operator138, Operator80",
    "Tooling": "Tool1",
    "BatchSize": 78,
    "Quantity": 849
  },
  {
    "WorkorderID": 89,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 08:04",
    "EndDateTime": "2024-10-03 14:04",
    "Process": "Conditioning",
    "Operators": "Operator5",
    "Tooling": "Tool24, Tool19, Tool3",
    "BatchSize": 78,
    "Quantity": 849
  },
  {
    "WorkorderID": 90,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator23, Operator124",
    "Tooling": "Tool20, Tool3, Tool8",
    "BatchSize": 99,
    "Quantity": 646
  },
  {
    "WorkorderID": 90,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 22:25",
    "EndDateTime": "2024-10-02 06:25",
    "Process": "Preparing",
    "Operators": "Operator92, Operator4, Operator63, Operator149",
    "Tooling": "Tool15",
    "BatchSize": 99,
    "Quantity": 646
  },
  {
    "WorkorderID": 90,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 09:29",
    "EndDateTime": "2024-10-02 17:29",
    "Process": "Silver Plating",
    "Operators": "Operator98, Operator64",
    "Tooling": "Tool14, Tool9",
    "BatchSize": 99,
    "Quantity": 646
  },
  {
    "WorkorderID": 90,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 08:23",
    "EndDateTime": "2024-10-03 14:23",
    "Process": "Polishing",
    "Operators": "Operator16, Operator20, Operator1, Operator129, Operator80",
    "Tooling": "Tool3",
    "BatchSize": 99,
    "Quantity": 646
  },
  {
    "WorkorderID": 90,
    "Product": "Vase",
    "StartDateTime": "2024-10-04 00:07",
    "EndDateTime": "2024-10-04 02:07",
    "Process": "Conditioning",
    "Operators": "Operator130, Operator86, Operator60",
    "Tooling": "Tool19, Tool20, Tool13",
    "BatchSize": 99,
    "Quantity": 646
  },
  {
    "WorkorderID": 91,
    "Product": "Tray",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator65, Operator64",
    "Tooling": "Tool6",
    "BatchSize": 77,
    "Quantity": 1234
  },
  {
    "WorkorderID": 91,
    "Product": "Tray",
    "StartDateTime": "2024-10-01 18:07",
    "EndDateTime": "2024-10-01 21:07",
    "Process": "Preparing",
    "Operators": "Operator16",
    "Tooling": "Tool29",
    "BatchSize": 77,
    "Quantity": 1234
  },
  {
    "WorkorderID": 91,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 03:44",
    "EndDateTime": "2024-10-02 10:44",
    "Process": "Silver Plating",
    "Operators": "Operator38, Operator149",
    "Tooling": "Tool21, Tool22, Tool8",
    "BatchSize": 77,
    "Quantity": 1234
  },
  {
    "WorkorderID": 91,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 08:51",
    "EndDateTime": "2024-10-03 11:51",
    "Process": "Polishing",
    "Operators": "Operator24",
    "Tooling": "Tool22, Tool23, Tool25",
    "BatchSize": 77,
    "Quantity": 1234
  },
  {
    "WorkorderID": 91,
    "Product": "Tray",
    "StartDateTime": "2024-10-04 08:54",
    "EndDateTime": "2024-10-04 10:54",
    "Process": "Conditioning",
    "Operators": "Operator109, Operator50",
    "Tooling": "Tool3",
    "BatchSize": 77,
    "Quantity": 1234
  },
  {
    "WorkorderID": 92,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator119, Operator30, Operator7, Operator14, Operator85",
    "Tooling": "Tool18",
    "BatchSize": 92,
    "Quantity": 1439
  },
  {
    "WorkorderID": 92,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 05:09",
    "EndDateTime": "2024-10-01 06:09",
    "Process": "Preparing",
    "Operators": "Operator126, Operator43",
    "Tooling": "Tool7, Tool15",
    "BatchSize": 92,
    "Quantity": 1439
  },
  {
    "WorkorderID": 92,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 10:08",
    "EndDateTime": "2024-10-01 16:08",
    "Process": "Silver Plating",
    "Operators": "Operator83, Operator99",
    "Tooling": "Tool14, Tool7, Tool24",
    "BatchSize": 92,
    "Quantity": 1439
  },
  {
    "WorkorderID": 92,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 19:50",
    "EndDateTime": "2024-10-01 21:50",
    "Process": "Polishing",
    "Operators": "Operator114, Operator141, Operator33",
    "Tooling": "Tool16, Tool22",
    "BatchSize": 92,
    "Quantity": 1439
  },
  {
    "WorkorderID": 92,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 05:50",
    "EndDateTime": "2024-10-02 09:50",
    "Process": "Conditioning",
    "Operators": "Operator13, Operator6, Operator90",
    "Tooling": "Tool28, Tool15, Tool9",
    "BatchSize": 92,
    "Quantity": 1439
  },
  {
    "WorkorderID": 93,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator4, Operator18, Operator117, Operator59, Operator136",
    "Tooling": "Tool1, Tool20, Tool2",
    "BatchSize": 142,
    "Quantity": 1201
  },
  {
    "WorkorderID": 93,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 17:30",
    "EndDateTime": "2024-10-01 19:30",
    "Process": "Preparing",
    "Operators": "Operator25, Operator50",
    "Tooling": "Tool5, Tool4, Tool11",
    "BatchSize": 142,
    "Quantity": 1201
  },
  {
    "WorkorderID": 93,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 20:45",
    "EndDateTime": "2024-10-02 00:45",
    "Process": "Silver Plating",
    "Operators": "Operator12, Operator36",
    "Tooling": "Tool22",
    "BatchSize": 142,
    "Quantity": 1201
  },
  {
    "WorkorderID": 93,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 22:45",
    "EndDateTime": "2024-10-03 06:45",
    "Process": "Polishing",
    "Operators": "Operator73, Operator97",
    "Tooling": "Tool18",
    "BatchSize": 142,
    "Quantity": 1201
  },
  {
    "WorkorderID": 93,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-04 01:46",
    "EndDateTime": "2024-10-04 04:46",
    "Process": "Conditioning",
    "Operators": "Operator142, Operator86, Operator92",
    "Tooling": "Tool19",
    "BatchSize": 142,
    "Quantity": 1201
  },
  {
    "WorkorderID": 94,
    "Product": "Cup",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator123, Operator11, Operator75",
    "Tooling": "Tool13, Tool19, Tool26",
    "BatchSize": 83,
    "Quantity": 1395
  },
  {
    "WorkorderID": 94,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 00:01",
    "EndDateTime": "2024-10-02 08:01",
    "Process": "Preparing",
    "Operators": "Operator117, Operator141",
    "Tooling": "Tool3, Tool14",
    "BatchSize": 83,
    "Quantity": 1395
  },
  {
    "WorkorderID": 94,
    "Product": "Cup",
    "StartDateTime": "2024-10-03 06:30",
    "EndDateTime": "2024-10-03 10:30",
    "Process": "Silver Plating",
    "Operators": "Operator60, Operator106",
    "Tooling": "Tool2, Tool9, Tool3",
    "BatchSize": 83,
    "Quantity": 1395
  },
  {
    "WorkorderID": 94,
    "Product": "Cup",
    "StartDateTime": "2024-10-03 14:44",
    "EndDateTime": "2024-10-03 17:44",
    "Process": "Polishing",
    "Operators": "Operator23, Operator17",
    "Tooling": "Tool4, Tool11, Tool12",
    "BatchSize": 83,
    "Quantity": 1395
  },
  {
    "WorkorderID": 94,
    "Product": "Cup",
    "StartDateTime": "2024-10-04 01:11",
    "EndDateTime": "2024-10-04 06:11",
    "Process": "Conditioning",
    "Operators": "Operator40",
    "Tooling": "Tool16, Tool18, Tool14",
    "BatchSize": 83,
    "Quantity": 1395
  },
  {
    "WorkorderID": 95,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator141, Operator48",
    "Tooling": "Tool14, Tool15",
    "BatchSize": 111,
    "Quantity": 641
  },
  {
    "WorkorderID": 95,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 12:25",
    "EndDateTime": "2024-10-01 14:25",
    "Process": "Preparing",
    "Operators": "Operator7",
    "Tooling": "Tool23, Tool21, Tool30",
    "BatchSize": 111,
    "Quantity": 641
  },
  {
    "WorkorderID": 95,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 04:23",
    "EndDateTime": "2024-10-02 05:23",
    "Process": "Silver Plating",
    "Operators": "Operator77",
    "Tooling": "Tool9",
    "BatchSize": 111,
    "Quantity": 641
  },
  {
    "WorkorderID": 95,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 08:25",
    "EndDateTime": "2024-10-02 13:25",
    "Process": "Polishing",
    "Operators": "Operator113",
    "Tooling": "Tool29, Tool12",
    "BatchSize": 111,
    "Quantity": 641
  },
  {
    "WorkorderID": 95,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 10:59",
    "EndDateTime": "2024-10-03 18:59",
    "Process": "Conditioning",
    "Operators": "Operator42, Operator143, Operator80, Operator97, Operator113",
    "Tooling": "Tool11",
    "BatchSize": 111,
    "Quantity": 641
  },
  {
    "WorkorderID": 96,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator116, Operator84, Operator51",
    "Tooling": "Tool9, Tool3",
    "BatchSize": 63,
    "Quantity": 1114
  },
  {
    "WorkorderID": 96,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 09:11",
    "EndDateTime": "2024-10-01 15:11",
    "Process": "Preparing",
    "Operators": "Operator15, Operator26, Operator19, Operator29, Operator93",
    "Tooling": "Tool8",
    "BatchSize": 63,
    "Quantity": 1114
  },
  {
    "WorkorderID": 96,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 15:57",
    "EndDateTime": "2024-10-01 17:57",
    "Process": "Silver Plating",
    "Operators": "Operator72",
    "Tooling": "Tool4",
    "BatchSize": 63,
    "Quantity": 1114
  },
  {
    "WorkorderID": 96,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 22:52",
    "EndDateTime": "2024-10-01 23:52",
    "Process": "Polishing",
    "Operators": "Operator140",
    "Tooling": "Tool17",
    "BatchSize": 63,
    "Quantity": 1114
  },
  {
    "WorkorderID": 96,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 17:48",
    "EndDateTime": "2024-10-03 01:48",
    "Process": "Conditioning",
    "Operators": "Operator95, Operator83, Operator115, Operator133",
    "Tooling": "Tool6, Tool27",
    "BatchSize": 63,
    "Quantity": 1114
  },
  {
    "WorkorderID": 97,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator123, Operator95, Operator87, Operator144",
    "Tooling": "Tool8, Tool19",
    "BatchSize": 100,
    "Quantity": 1023
  },
  {
    "WorkorderID": 97,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 00:41",
    "EndDateTime": "2024-10-02 03:41",
    "Process": "Preparing",
    "Operators": "Operator102, Operator42",
    "Tooling": "Tool21, Tool18",
    "BatchSize": 100,
    "Quantity": 1023
  },
  {
    "WorkorderID": 97,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 11:04",
    "EndDateTime": "2024-10-02 14:04",
    "Process": "Silver Plating",
    "Operators": "Operator144, Operator135, Operator5",
    "Tooling": "Tool25",
    "BatchSize": 100,
    "Quantity": 1023
  },
  {
    "WorkorderID": 97,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 18:05",
    "EndDateTime": "2024-10-03 02:05",
    "Process": "Polishing",
    "Operators": "Operator144, Operator30, Operator35, Operator15",
    "Tooling": "Tool6, Tool25",
    "BatchSize": 100,
    "Quantity": 1023
  },
  {
    "WorkorderID": 97,
    "Product": "Knife",
    "StartDateTime": "2024-10-03 07:06",
    "EndDateTime": "2024-10-03 10:06",
    "Process": "Conditioning",
    "Operators": "Operator113, Operator39, Operator126",
    "Tooling": "Tool28, Tool20",
    "BatchSize": 100,
    "Quantity": 1023
  },
  {
    "WorkorderID": 98,
    "Product": "Cup",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator80",
    "Tooling": "Tool26, Tool4, Tool14",
    "BatchSize": 59,
    "Quantity": 702
  },
  {
    "WorkorderID": 98,
    "Product": "Cup",
    "StartDateTime": "2024-10-01 19:01",
    "EndDateTime": "2024-10-02 00:01",
    "Process": "Preparing",
    "Operators": "Operator133, Operator41, Operator26",
    "Tooling": "Tool29, Tool5",
    "BatchSize": 59,
    "Quantity": 702
  },
  {
    "WorkorderID": 98,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 10:08",
    "EndDateTime": "2024-10-02 17:08",
    "Process": "Silver Plating",
    "Operators": "Operator28, Operator60, Operator11",
    "Tooling": "Tool5, Tool1, Tool28",
    "BatchSize": 59,
    "Quantity": 702
  },
  {
    "WorkorderID": 98,
    "Product": "Cup",
    "StartDateTime": "2024-10-03 08:46",
    "EndDateTime": "2024-10-03 13:46",
    "Process": "Polishing",
    "Operators": "Operator141, Operator67, Operator80, Operator116",
    "Tooling": "Tool12",
    "BatchSize": 59,
    "Quantity": 702
  },
  {
    "WorkorderID": 98,
    "Product": "Cup",
    "StartDateTime": "2024-10-04 00:44",
    "EndDateTime": "2024-10-04 04:44",
    "Process": "Conditioning",
    "Operators": "Operator36, Operator113, Operator143, Operator62",
    "Tooling": "Tool13",
    "BatchSize": 59,
    "Quantity": 702
  },
  {
    "WorkorderID": 99,
    "Product": "Knife",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator105, Operator49",
    "Tooling": "Tool14, Tool7, Tool1",
    "BatchSize": 96,
    "Quantity": 543
  },
  {
    "WorkorderID": 99,
    "Product": "Knife",
    "StartDateTime": "2024-10-01 10:05",
    "EndDateTime": "2024-10-01 13:05",
    "Process": "Preparing",
    "Operators": "Operator93, Operator125, Operator131",
    "Tooling": "Tool2, Tool1",
    "BatchSize": 96,
    "Quantity": 543
  },
  {
    "WorkorderID": 99,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 01:08",
    "EndDateTime": "2024-10-02 09:08",
    "Process": "Silver Plating",
    "Operators": "Operator107",
    "Tooling": "Tool27, Tool19",
    "BatchSize": 96,
    "Quantity": 543
  },
  {
    "WorkorderID": 99,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 11:45",
    "EndDateTime": "2024-10-02 12:45",
    "Process": "Polishing",
    "Operators": "Operator34, Operator87, Operator109, Operator27",
    "Tooling": "Tool27, Tool23",
    "BatchSize": 96,
    "Quantity": 543
  },
  {
    "WorkorderID": 99,
    "Product": "Knife",
    "StartDateTime": "2024-10-02 22:12",
    "EndDateTime": "2024-10-03 01:12",
    "Process": "Conditioning",
    "Operators": "Operator29, Operator138, Operator109, Operator5",
    "Tooling": "Tool19",
    "BatchSize": 96,
    "Quantity": 543
  },
  {
    "WorkorderID": 100,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator139, Operator57",
    "Tooling": "Tool8, Tool19",
    "BatchSize": 99,
    "Quantity": 562
  },
  {
    "WorkorderID": 100,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 04:45",
    "EndDateTime": "2024-10-01 07:45",
    "Process": "Preparing",
    "Operators": "Operator96, Operator139",
    "Tooling": "Tool1, Tool8, Tool30",
    "BatchSize": 99,
    "Quantity": 562
  },
  {
    "WorkorderID": 100,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 08:36",
    "EndDateTime": "2024-10-01 09:36",
    "Process": "Silver Plating",
    "Operators": "Operator67",
    "Tooling": "Tool1, Tool27, Tool19",
    "BatchSize": 99,
    "Quantity": 562
  },
  {
    "WorkorderID": 100,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 06:35",
    "EndDateTime": "2024-10-02 08:35",
    "Process": "Polishing",
    "Operators": "Operator39",
    "Tooling": "Tool24, Tool9, Tool19",
    "BatchSize": 99,
    "Quantity": 562
  },
  {
    "WorkorderID": 100,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 08:17",
    "EndDateTime": "2024-10-03 09:17",
    "Process": "Conditioning",
    "Operators": "Operator56, Operator86, Operator112",
    "Tooling": "Tool17, Tool29",
    "BatchSize": 99,
    "Quantity": 562
  },
  {
    "WorkorderID": 101,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator146, Operator122, Operator139",
    "Tooling": "Tool1, Tool17, Tool2",
    "BatchSize": 148,
    "Quantity": 1237
  },
  {
    "WorkorderID": 101,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 15:37",
    "EndDateTime": "2024-10-01 20:37",
    "Process": "Preparing",
    "Operators": "Operator45",
    "Tooling": "Tool20, Tool4",
    "BatchSize": 148,
    "Quantity": 1237
  },
  {
    "WorkorderID": 101,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 21:57",
    "EndDateTime": "2024-10-01 23:57",
    "Process": "Silver Plating",
    "Operators": "Operator103, Operator17",
    "Tooling": "Tool3, Tool19",
    "BatchSize": 148,
    "Quantity": 1237
  },
  {
    "WorkorderID": 101,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 09:34",
    "EndDateTime": "2024-10-02 16:34",
    "Process": "Polishing",
    "Operators": "Operator40, Operator28, Operator93",
    "Tooling": "Tool3, Tool29",
    "BatchSize": 148,
    "Quantity": 1237
  },
  {
    "WorkorderID": 101,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 17:34",
    "EndDateTime": "2024-10-02 23:34",
    "Process": "Conditioning",
    "Operators": "Operator61, Operator124, Operator48, Operator122, Operator132",
    "Tooling": "Tool13",
    "BatchSize": 148,
    "Quantity": 1237
  },
  {
    "WorkorderID": 102,
    "Product": "Tray",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator7, Operator122, Operator51, Operator97, Operator124",
    "Tooling": "Tool13, Tool16, Tool3",
    "BatchSize": 62,
    "Quantity": 1323
  },
  {
    "WorkorderID": 102,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 00:48",
    "EndDateTime": "2024-10-02 03:48",
    "Process": "Preparing",
    "Operators": "Operator127, Operator136",
    "Tooling": "Tool3, Tool4",
    "BatchSize": 62,
    "Quantity": 1323
  },
  {
    "WorkorderID": 102,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 13:54",
    "EndDateTime": "2024-10-02 20:54",
    "Process": "Silver Plating",
    "Operators": "Operator9, Operator45",
    "Tooling": "Tool6",
    "BatchSize": 62,
    "Quantity": 1323
  },
  {
    "WorkorderID": 102,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 16:11",
    "EndDateTime": "2024-10-03 17:11",
    "Process": "Polishing",
    "Operators": "Operator77, Operator100, Operator9, Operator117",
    "Tooling": "Tool11, Tool26, Tool19",
    "BatchSize": 62,
    "Quantity": 1323
  },
  {
    "WorkorderID": 102,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 19:31",
    "EndDateTime": "2024-10-03 21:31",
    "Process": "Conditioning",
    "Operators": "Operator141",
    "Tooling": "Tool16, Tool20",
    "BatchSize": 62,
    "Quantity": 1323
  },
  {
    "WorkorderID": 103,
    "Product": "Saucepan",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator81, Operator44, Operator102",
    "Tooling": "Tool1, Tool16, Tool26",
    "BatchSize": 129,
    "Quantity": 1233
  },
  {
    "WorkorderID": 103,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-01 22:50",
    "EndDateTime": "2024-10-02 03:50",
    "Process": "Preparing",
    "Operators": "Operator65, Operator72, Operator127, Operator81, Operator144",
    "Tooling": "Tool10, Tool2, Tool17",
    "BatchSize": 129,
    "Quantity": 1233
  },
  {
    "WorkorderID": 103,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-02 13:35",
    "EndDateTime": "2024-10-02 20:35",
    "Process": "Silver Plating",
    "Operators": "Operator132, Operator14, Operator62, Operator71, Operator52",
    "Tooling": "Tool23",
    "BatchSize": 129,
    "Quantity": 1233
  },
  {
    "WorkorderID": 103,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-03 07:31",
    "EndDateTime": "2024-10-03 10:31",
    "Process": "Polishing",
    "Operators": "Operator79, Operator143, Operator51",
    "Tooling": "Tool5, Tool18, Tool15",
    "BatchSize": 129,
    "Quantity": 1233
  },
  {
    "WorkorderID": 103,
    "Product": "Saucepan",
    "StartDateTime": "2024-10-04 06:18",
    "EndDateTime": "2024-10-04 09:18",
    "Process": "Conditioning",
    "Operators": "Operator91, Operator83, Operator56",
    "Tooling": "Tool16, Tool7",
    "BatchSize": 129,
    "Quantity": 1233
  },
  {
    "WorkorderID": 104,
    "Product": "Coaster",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator34",
    "Tooling": "Tool10, Tool16, Tool3",
    "BatchSize": 75,
    "Quantity": 951
  },
  {
    "WorkorderID": 104,
    "Product": "Coaster",
    "StartDateTime": "2024-10-01 21:30",
    "EndDateTime": "2024-10-02 04:30",
    "Process": "Preparing",
    "Operators": "Operator128, Operator117, Operator57, Operator56, Operator49",
    "Tooling": "Tool8, Tool20, Tool7",
    "BatchSize": 75,
    "Quantity": 951
  },
  {
    "WorkorderID": 104,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 02:50",
    "EndDateTime": "2024-10-03 10:50",
    "Process": "Silver Plating",
    "Operators": "Operator46, Operator20, Operator140, Operator24, Operator108",
    "Tooling": "Tool14, Tool5, Tool10",
    "BatchSize": 75,
    "Quantity": 951
  },
  {
    "WorkorderID": 104,
    "Product": "Coaster",
    "StartDateTime": "2024-10-03 18:20",
    "EndDateTime": "2024-10-03 22:20",
    "Process": "Polishing",
    "Operators": "Operator62",
    "Tooling": "Tool4, Tool11",
    "BatchSize": 75,
    "Quantity": 951
  },
  {
    "WorkorderID": 104,
    "Product": "Coaster",
    "StartDateTime": "2024-10-04 14:54",
    "EndDateTime": "2024-10-04 19:54",
    "Process": "Conditioning",
    "Operators": "Operator139, Operator32, Operator113, Operator62",
    "Tooling": "Tool3, Tool4, Tool8",
    "BatchSize": 75,
    "Quantity": 951
  },
  {
    "WorkorderID": 105,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator32, Operator43",
    "Tooling": "Tool25",
    "BatchSize": 115,
    "Quantity": 1496
  },
  {
    "WorkorderID": 105,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 08:04",
    "EndDateTime": "2024-10-01 13:04",
    "Process": "Preparing",
    "Operators": "Operator32, Operator50",
    "Tooling": "Tool6, Tool15, Tool16",
    "BatchSize": 115,
    "Quantity": 1496
  },
  {
    "WorkorderID": 105,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 21:59",
    "EndDateTime": "2024-10-02 00:59",
    "Process": "Silver Plating",
    "Operators": "Operator48",
    "Tooling": "Tool26, Tool16, Tool29",
    "BatchSize": 115,
    "Quantity": 1496
  },
  {
    "WorkorderID": 105,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 10:34",
    "EndDateTime": "2024-10-02 11:34",
    "Process": "Polishing",
    "Operators": "Operator51, Operator6, Operator12",
    "Tooling": "Tool27",
    "BatchSize": 115,
    "Quantity": 1496
  },
  {
    "WorkorderID": 105,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 16:32",
    "EndDateTime": "2024-10-02 19:32",
    "Process": "Conditioning",
    "Operators": "Operator62, Operator111, Operator139, Operator87",
    "Tooling": "Tool4",
    "BatchSize": 115,
    "Quantity": 1496
  },
  {
    "WorkorderID": 106,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator100, Operator79, Operator97",
    "Tooling": "Tool4, Tool20",
    "BatchSize": 116,
    "Quantity": 1003
  },
  {
    "WorkorderID": 106,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 04:34",
    "EndDateTime": "2024-10-02 09:34",
    "Process": "Preparing",
    "Operators": "Operator98",
    "Tooling": "Tool28, Tool16, Tool11",
    "BatchSize": 116,
    "Quantity": 1003
  },
  {
    "WorkorderID": 106,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 02:29",
    "EndDateTime": "2024-10-03 04:29",
    "Process": "Silver Plating",
    "Operators": "Operator74",
    "Tooling": "Tool17",
    "BatchSize": 116,
    "Quantity": 1003
  },
  {
    "WorkorderID": 106,
    "Product": "Jug",
    "StartDateTime": "2024-10-04 03:41",
    "EndDateTime": "2024-10-04 07:41",
    "Process": "Polishing",
    "Operators": "Operator26, Operator36, Operator22, Operator25, Operator148",
    "Tooling": "Tool28, Tool10",
    "BatchSize": 116,
    "Quantity": 1003
  },
  {
    "WorkorderID": 106,
    "Product": "Jug",
    "StartDateTime": "2024-10-05 02:57",
    "EndDateTime": "2024-10-05 04:57",
    "Process": "Conditioning",
    "Operators": "Operator98, Operator149",
    "Tooling": "Tool30",
    "BatchSize": 116,
    "Quantity": 1003
  },
  {
    "WorkorderID": 107,
    "Product": "Tray",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator78, Operator102, Operator46",
    "Tooling": "Tool28, Tool29",
    "BatchSize": 95,
    "Quantity": 1443
  },
  {
    "WorkorderID": 107,
    "Product": "Tray",
    "StartDateTime": "2024-10-01 10:57",
    "EndDateTime": "2024-10-01 12:57",
    "Process": "Preparing",
    "Operators": "Operator109, Operator11",
    "Tooling": "Tool8",
    "BatchSize": 95,
    "Quantity": 1443
  },
  {
    "WorkorderID": 107,
    "Product": "Tray",
    "StartDateTime": "2024-10-01 15:06",
    "EndDateTime": "2024-10-01 21:06",
    "Process": "Silver Plating",
    "Operators": "Operator80",
    "Tooling": "Tool25, Tool5",
    "BatchSize": 95,
    "Quantity": 1443
  },
  {
    "WorkorderID": 107,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 08:12",
    "EndDateTime": "2024-10-02 15:12",
    "Process": "Polishing",
    "Operators": "Operator85, Operator136, Operator109, Operator116, Operator26",
    "Tooling": "Tool25, Tool24",
    "BatchSize": 95,
    "Quantity": 1443
  },
  {
    "WorkorderID": 107,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 10:25",
    "EndDateTime": "2024-10-03 16:25",
    "Process": "Conditioning",
    "Operators": "Operator66, Operator124",
    "Tooling": "Tool9, Tool4",
    "BatchSize": 95,
    "Quantity": 1443
  },
  {
    "WorkorderID": 108,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator141, Operator71, Operator32, Operator6",
    "Tooling": "Tool8",
    "BatchSize": 75,
    "Quantity": 837
  },
  {
    "WorkorderID": 108,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 15:42",
    "EndDateTime": "2024-10-01 23:42",
    "Process": "Preparing",
    "Operators": "Operator103, Operator37, Operator14, Operator47, Operator120",
    "Tooling": "Tool4",
    "BatchSize": 75,
    "Quantity": 837
  },
  {
    "WorkorderID": 108,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 23:49",
    "EndDateTime": "2024-10-02 00:49",
    "Process": "Silver Plating",
    "Operators": "Operator40, Operator123, Operator109, Operator147, Operator125",
    "Tooling": "Tool17, Tool9, Tool13",
    "BatchSize": 75,
    "Quantity": 837
  },
  {
    "WorkorderID": 108,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 04:32",
    "EndDateTime": "2024-10-02 08:32",
    "Process": "Polishing",
    "Operators": "Operator37, Operator70",
    "Tooling": "Tool14, Tool19, Tool10",
    "BatchSize": 75,
    "Quantity": 837
  },
  {
    "WorkorderID": 108,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 00:38",
    "EndDateTime": "2024-10-03 07:38",
    "Process": "Conditioning",
    "Operators": "Operator144, Operator132, Operator37, Operator70",
    "Tooling": "Tool10, Tool3",
    "BatchSize": 75,
    "Quantity": 837
  },
  {
    "WorkorderID": 109,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator101, Operator62",
    "Tooling": "Tool3",
    "BatchSize": 128,
    "Quantity": 624
  },
  {
    "WorkorderID": 109,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 23:06",
    "EndDateTime": "2024-10-02 01:06",
    "Process": "Preparing",
    "Operators": "Operator144",
    "Tooling": "Tool13, Tool15",
    "BatchSize": 128,
    "Quantity": 624
  },
  {
    "WorkorderID": 109,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 10:59",
    "EndDateTime": "2024-10-02 16:59",
    "Process": "Silver Plating",
    "Operators": "Operator134, Operator63",
    "Tooling": "Tool12, Tool13",
    "BatchSize": 128,
    "Quantity": 624
  },
  {
    "WorkorderID": 109,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 08:11",
    "EndDateTime": "2024-10-03 10:11",
    "Process": "Polishing",
    "Operators": "Operator147, Operator80",
    "Tooling": "Tool23, Tool12, Tool16",
    "BatchSize": 128,
    "Quantity": 624
  },
  {
    "WorkorderID": 109,
    "Product": "Jug",
    "StartDateTime": "2024-10-04 06:34",
    "EndDateTime": "2024-10-04 07:34",
    "Process": "Conditioning",
    "Operators": "Operator41, Operator127, Operator70, Operator129, Operator68",
    "Tooling": "Tool23",
    "BatchSize": 128,
    "Quantity": 624
  },
  {
    "WorkorderID": 110,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator12, Operator68, Operator115, Operator129, Operator143",
    "Tooling": "Tool11, Tool30, Tool7",
    "BatchSize": 55,
    "Quantity": 769
  },
  {
    "WorkorderID": 110,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 18:08",
    "EndDateTime": "2024-10-01 20:08",
    "Process": "Preparing",
    "Operators": "Operator111, Operator96, Operator52",
    "Tooling": "Tool11, Tool29, Tool8",
    "BatchSize": 55,
    "Quantity": 769
  },
  {
    "WorkorderID": 110,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 03:06",
    "EndDateTime": "2024-10-02 10:06",
    "Process": "Silver Plating",
    "Operators": "Operator111, Operator49, Operator75",
    "Tooling": "Tool10, Tool8, Tool19",
    "BatchSize": 55,
    "Quantity": 769
  },
  {
    "WorkorderID": 110,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 20:49",
    "EndDateTime": "2024-10-03 02:49",
    "Process": "Polishing",
    "Operators": "Operator79, Operator72, Operator34",
    "Tooling": "Tool10",
    "BatchSize": 55,
    "Quantity": 769
  },
  {
    "WorkorderID": 110,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 13:54",
    "EndDateTime": "2024-10-03 16:54",
    "Process": "Conditioning",
    "Operators": "Operator135, Operator145, Operator68",
    "Tooling": "Tool29, Tool7, Tool5",
    "BatchSize": 55,
    "Quantity": 769
  },
  {
    "WorkorderID": 111,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator65, Operator139",
    "Tooling": "Tool9, Tool25, Tool23",
    "BatchSize": 117,
    "Quantity": 1291
  },
  {
    "WorkorderID": 111,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 01:10",
    "EndDateTime": "2024-10-01 05:10",
    "Process": "Preparing",
    "Operators": "Operator110, Operator46, Operator67, Operator86",
    "Tooling": "Tool11, Tool29",
    "BatchSize": 117,
    "Quantity": 1291
  },
  {
    "WorkorderID": 111,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 10:41",
    "EndDateTime": "2024-10-01 13:41",
    "Process": "Silver Plating",
    "Operators": "Operator144, Operator99, Operator2, Operator1, Operator71",
    "Tooling": "Tool1, Tool28",
    "BatchSize": 117,
    "Quantity": 1291
  },
  {
    "WorkorderID": 111,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 00:37",
    "EndDateTime": "2024-10-02 07:37",
    "Process": "Polishing",
    "Operators": "Operator102, Operator94",
    "Tooling": "Tool30, Tool5, Tool23",
    "BatchSize": 117,
    "Quantity": 1291
  },
  {
    "WorkorderID": 111,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 21:01",
    "EndDateTime": "2024-10-02 23:01",
    "Process": "Conditioning",
    "Operators": "Operator138",
    "Tooling": "Tool13",
    "BatchSize": 117,
    "Quantity": 1291
  },
  {
    "WorkorderID": 112,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator144",
    "Tooling": "Tool13",
    "BatchSize": 67,
    "Quantity": 1235
  },
  {
    "WorkorderID": 112,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 21:33",
    "EndDateTime": "2024-10-01 23:33",
    "Process": "Preparing",
    "Operators": "Operator36, Operator44, Operator59, Operator141, Operator14",
    "Tooling": "Tool15, Tool8",
    "BatchSize": 67,
    "Quantity": 1235
  },
  {
    "WorkorderID": 112,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 11:28",
    "EndDateTime": "2024-10-02 18:28",
    "Process": "Silver Plating",
    "Operators": "Operator139",
    "Tooling": "Tool14",
    "BatchSize": 67,
    "Quantity": 1235
  },
  {
    "WorkorderID": 112,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 01:35",
    "EndDateTime": "2024-10-03 05:35",
    "Process": "Polishing",
    "Operators": "Operator113, Operator8, Operator10, Operator150",
    "Tooling": "Tool12",
    "BatchSize": 67,
    "Quantity": 1235
  },
  {
    "WorkorderID": 112,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 18:03",
    "EndDateTime": "2024-10-04 01:03",
    "Process": "Conditioning",
    "Operators": "Operator57, Operator104, Operator20",
    "Tooling": "Tool27, Tool12",
    "BatchSize": 67,
    "Quantity": 1235
  },
  {
    "WorkorderID": 113,
    "Product": "Bowl",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator6, Operator74",
    "Tooling": "Tool27, Tool23",
    "BatchSize": 51,
    "Quantity": 1358
  },
  {
    "WorkorderID": 113,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 12:52",
    "EndDateTime": "2024-10-01 18:52",
    "Process": "Preparing",
    "Operators": "Operator28",
    "Tooling": "Tool15, Tool24",
    "BatchSize": 51,
    "Quantity": 1358
  },
  {
    "WorkorderID": 113,
    "Product": "Bowl",
    "StartDateTime": "2024-10-02 14:04",
    "EndDateTime": "2024-10-02 22:04",
    "Process": "Silver Plating",
    "Operators": "Operator46, Operator50, Operator136",
    "Tooling": "Tool29",
    "BatchSize": 51,
    "Quantity": 1358
  },
  {
    "WorkorderID": 113,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 11:41",
    "EndDateTime": "2024-10-03 12:41",
    "Process": "Polishing",
    "Operators": "Operator13, Operator123, Operator26, Operator46",
    "Tooling": "Tool24",
    "BatchSize": 51,
    "Quantity": 1358
  },
  {
    "WorkorderID": 113,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 19:12",
    "EndDateTime": "2024-10-03 23:12",
    "Process": "Conditioning",
    "Operators": "Operator36, Operator41, Operator34, Operator50",
    "Tooling": "Tool3, Tool26, Tool19",
    "BatchSize": 51,
    "Quantity": 1358
  },
  {
    "WorkorderID": 114,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator113, Operator137",
    "Tooling": "Tool22, Tool7",
    "BatchSize": 94,
    "Quantity": 943
  },
  {
    "WorkorderID": 114,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 21:29",
    "EndDateTime": "2024-10-02 03:29",
    "Process": "Preparing",
    "Operators": "Operator2, Operator15, Operator101, Operator59, Operator113",
    "Tooling": "Tool12, Tool16, Tool15",
    "BatchSize": 94,
    "Quantity": 943
  },
  {
    "WorkorderID": 114,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 11:22",
    "EndDateTime": "2024-10-02 15:22",
    "Process": "Silver Plating",
    "Operators": "Operator102, Operator49",
    "Tooling": "Tool17, Tool9",
    "BatchSize": 94,
    "Quantity": 943
  },
  {
    "WorkorderID": 114,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 13:30",
    "EndDateTime": "2024-10-03 15:30",
    "Process": "Polishing",
    "Operators": "Operator27, Operator53",
    "Tooling": "Tool13",
    "BatchSize": 94,
    "Quantity": 943
  },
  {
    "WorkorderID": 114,
    "Product": "Teapot",
    "StartDateTime": "2024-10-04 09:08",
    "EndDateTime": "2024-10-04 10:08",
    "Process": "Conditioning",
    "Operators": "Operator18, Operator17, Operator83",
    "Tooling": "Tool29, Tool13",
    "BatchSize": 94,
    "Quantity": 943
  },
  {
    "WorkorderID": 115,
    "Product": "Bowl",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator130",
    "Tooling": "Tool3",
    "BatchSize": 144,
    "Quantity": 1482
  },
  {
    "WorkorderID": 115,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 10:23",
    "EndDateTime": "2024-10-01 16:23",
    "Process": "Preparing",
    "Operators": "Operator133, Operator24, Operator105, Operator141",
    "Tooling": "Tool16, Tool4",
    "BatchSize": 144,
    "Quantity": 1482
  },
  {
    "WorkorderID": 115,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 19:00",
    "EndDateTime": "2024-10-02 01:00",
    "Process": "Silver Plating",
    "Operators": "Operator66, Operator25, Operator39, Operator87, Operator119",
    "Tooling": "Tool16",
    "BatchSize": 144,
    "Quantity": 1482
  },
  {
    "WorkorderID": 115,
    "Product": "Bowl",
    "StartDateTime": "2024-10-02 02:01",
    "EndDateTime": "2024-10-02 09:01",
    "Process": "Polishing",
    "Operators": "Operator67, Operator137, Operator23",
    "Tooling": "Tool23",
    "BatchSize": 144,
    "Quantity": 1482
  },
  {
    "WorkorderID": 115,
    "Product": "Bowl",
    "StartDateTime": "2024-10-02 10:38",
    "EndDateTime": "2024-10-02 11:38",
    "Process": "Conditioning",
    "Operators": "Operator140, Operator119, Operator45, Operator63, Operator54",
    "Tooling": "Tool23",
    "BatchSize": 144,
    "Quantity": 1482
  },
  {
    "WorkorderID": 116,
    "Product": "Cup",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator121, Operator82",
    "Tooling": "Tool6, Tool22",
    "BatchSize": 75,
    "Quantity": 1200
  },
  {
    "WorkorderID": 116,
    "Product": "Cup",
    "StartDateTime": "2024-10-01 20:25",
    "EndDateTime": "2024-10-01 22:25",
    "Process": "Preparing",
    "Operators": "Operator41, Operator102",
    "Tooling": "Tool22",
    "BatchSize": 75,
    "Quantity": 1200
  },
  {
    "WorkorderID": 116,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 21:47",
    "EndDateTime": "2024-10-03 05:47",
    "Process": "Silver Plating",
    "Operators": "Operator34, Operator25, Operator102",
    "Tooling": "Tool22, Tool19",
    "BatchSize": 75,
    "Quantity": 1200
  },
  {
    "WorkorderID": 116,
    "Product": "Cup",
    "StartDateTime": "2024-10-03 13:11",
    "EndDateTime": "2024-10-03 21:11",
    "Process": "Polishing",
    "Operators": "Operator116, Operator93, Operator60, Operator117",
    "Tooling": "Tool3, Tool15",
    "BatchSize": 75,
    "Quantity": 1200
  },
  {
    "WorkorderID": 116,
    "Product": "Cup",
    "StartDateTime": "2024-10-04 20:53",
    "EndDateTime": "2024-10-04 22:53",
    "Process": "Conditioning",
    "Operators": "Operator75",
    "Tooling": "Tool9",
    "BatchSize": 75,
    "Quantity": 1200
  },
  {
    "WorkorderID": 117,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator125, Operator101",
    "Tooling": "Tool2, Tool7",
    "BatchSize": 96,
    "Quantity": 606
  },
  {
    "WorkorderID": 117,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 18:57",
    "EndDateTime": "2024-10-01 19:57",
    "Process": "Preparing",
    "Operators": "Operator52, Operator32, Operator21, Operator138, Operator116",
    "Tooling": "Tool12, Tool26, Tool22",
    "BatchSize": 96,
    "Quantity": 606
  },
  {
    "WorkorderID": 117,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 09:01",
    "EndDateTime": "2024-10-02 12:01",
    "Process": "Silver Plating",
    "Operators": "Operator52, Operator121, Operator32",
    "Tooling": "Tool3, Tool4, Tool26",
    "BatchSize": 96,
    "Quantity": 606
  },
  {
    "WorkorderID": 117,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 18:09",
    "EndDateTime": "2024-10-03 00:09",
    "Process": "Polishing",
    "Operators": "Operator8, Operator88, Operator132",
    "Tooling": "Tool24, Tool29",
    "BatchSize": 96,
    "Quantity": 606
  },
  {
    "WorkorderID": 117,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 00:17",
    "EndDateTime": "2024-10-03 02:17",
    "Process": "Conditioning",
    "Operators": "Operator112, Operator110",
    "Tooling": "Tool22",
    "BatchSize": 96,
    "Quantity": 606
  },
  {
    "WorkorderID": 118,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator112, Operator24, Operator36, Operator21",
    "Tooling": "Tool23",
    "BatchSize": 89,
    "Quantity": 540
  },
  {
    "WorkorderID": 118,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 13:30",
    "EndDateTime": "2024-10-01 15:30",
    "Process": "Preparing",
    "Operators": "Operator24",
    "Tooling": "Tool24",
    "BatchSize": 89,
    "Quantity": 540
  },
  {
    "WorkorderID": 118,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 09:04",
    "EndDateTime": "2024-10-02 11:04",
    "Process": "Silver Plating",
    "Operators": "Operator81, Operator142, Operator19, Operator140",
    "Tooling": "Tool28, Tool22, Tool19",
    "BatchSize": 89,
    "Quantity": 540
  },
  {
    "WorkorderID": 118,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 18:56",
    "EndDateTime": "2024-10-03 01:56",
    "Process": "Polishing",
    "Operators": "Operator93, Operator143, Operator78, Operator128",
    "Tooling": "Tool22, Tool21, Tool27",
    "BatchSize": 89,
    "Quantity": 540
  },
  {
    "WorkorderID": 118,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 10:59",
    "EndDateTime": "2024-10-03 13:59",
    "Process": "Conditioning",
    "Operators": "Operator69, Operator79, Operator52, Operator81, Operator94",
    "Tooling": "Tool18",
    "BatchSize": 89,
    "Quantity": 540
  },
  {
    "WorkorderID": 119,
    "Product": "Fork",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator47, Operator56, Operator89, Operator137, Operator82",
    "Tooling": "Tool21",
    "BatchSize": 80,
    "Quantity": 599
  },
  {
    "WorkorderID": 119,
    "Product": "Fork",
    "StartDateTime": "2024-10-01 13:36",
    "EndDateTime": "2024-10-01 16:36",
    "Process": "Preparing",
    "Operators": "Operator119, Operator150, Operator67, Operator142, Operator121",
    "Tooling": "Tool10, Tool1",
    "BatchSize": 80,
    "Quantity": 599
  },
  {
    "WorkorderID": 119,
    "Product": "Fork",
    "StartDateTime": "2024-10-02 15:01",
    "EndDateTime": "2024-10-02 16:01",
    "Process": "Silver Plating",
    "Operators": "Operator98, Operator94, Operator86, Operator124",
    "Tooling": "Tool3, Tool11",
    "BatchSize": 80,
    "Quantity": 599
  },
  {
    "WorkorderID": 119,
    "Product": "Fork",
    "StartDateTime": "2024-10-03 04:57",
    "EndDateTime": "2024-10-03 10:57",
    "Process": "Polishing",
    "Operators": "Operator139, Operator129, Operator97",
    "Tooling": "Tool28, Tool16",
    "BatchSize": 80,
    "Quantity": 599
  },
  {
    "WorkorderID": 119,
    "Product": "Fork",
    "StartDateTime": "2024-10-03 21:35",
    "EndDateTime": "2024-10-04 01:35",
    "Process": "Conditioning",
    "Operators": "Operator70, Operator63, Operator28, Operator13",
    "Tooling": "Tool21, Tool1",
    "BatchSize": 80,
    "Quantity": 599
  },
  {
    "WorkorderID": 120,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator110, Operator7, Operator28",
    "Tooling": "Tool28, Tool8, Tool17",
    "BatchSize": 108,
    "Quantity": 666
  },
  {
    "WorkorderID": 120,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 01:01",
    "EndDateTime": "2024-10-02 08:01",
    "Process": "Preparing",
    "Operators": "Operator5, Operator69, Operator26, Operator74, Operator119",
    "Tooling": "Tool24, Tool2, Tool15",
    "BatchSize": 108,
    "Quantity": 666
  },
  {
    "WorkorderID": 120,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 08:43",
    "EndDateTime": "2024-10-02 09:43",
    "Process": "Silver Plating",
    "Operators": "Operator49, Operator82, Operator131, Operator41",
    "Tooling": "Tool27, Tool24, Tool26",
    "BatchSize": 108,
    "Quantity": 666
  },
  {
    "WorkorderID": 120,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 20:35",
    "EndDateTime": "2024-10-02 23:35",
    "Process": "Polishing",
    "Operators": "Operator62, Operator141, Operator34",
    "Tooling": "Tool25, Tool27, Tool7",
    "BatchSize": 108,
    "Quantity": 666
  },
  {
    "WorkorderID": 120,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 02:47",
    "EndDateTime": "2024-10-03 08:47",
    "Process": "Conditioning",
    "Operators": "Operator4, Operator48",
    "Tooling": "Tool12",
    "BatchSize": 108,
    "Quantity": 666
  },
  {
    "WorkorderID": 121,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator13, Operator27, Operator145, Operator28",
    "Tooling": "Tool27, Tool12",
    "BatchSize": 134,
    "Quantity": 1087
  },
  {
    "WorkorderID": 121,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 16:45",
    "EndDateTime": "2024-10-01 21:45",
    "Process": "Preparing",
    "Operators": "Operator118, Operator28, Operator134",
    "Tooling": "Tool7, Tool27, Tool29",
    "BatchSize": 134,
    "Quantity": 1087
  },
  {
    "WorkorderID": 121,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 22:54",
    "EndDateTime": "2024-10-02 03:54",
    "Process": "Silver Plating",
    "Operators": "Operator136, Operator24, Operator31",
    "Tooling": "Tool30",
    "BatchSize": 134,
    "Quantity": 1087
  },
  {
    "WorkorderID": 121,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 04:21",
    "EndDateTime": "2024-10-02 06:21",
    "Process": "Polishing",
    "Operators": "Operator132, Operator61, Operator50, Operator133, Operator37",
    "Tooling": "Tool8",
    "BatchSize": 134,
    "Quantity": 1087
  },
  {
    "WorkorderID": 121,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 09:24",
    "EndDateTime": "2024-10-02 11:24",
    "Process": "Conditioning",
    "Operators": "Operator147",
    "Tooling": "Tool3, Tool22, Tool30",
    "BatchSize": 134,
    "Quantity": 1087
  },
  {
    "WorkorderID": 122,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator138, Operator149",
    "Tooling": "Tool23, Tool24",
    "BatchSize": 149,
    "Quantity": 1359
  },
  {
    "WorkorderID": 122,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 07:18",
    "EndDateTime": "2024-10-01 08:18",
    "Process": "Preparing",
    "Operators": "Operator63, Operator30, Operator130",
    "Tooling": "Tool26, Tool21",
    "BatchSize": 149,
    "Quantity": 1359
  },
  {
    "WorkorderID": 122,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 20:00",
    "EndDateTime": "2024-10-02 01:00",
    "Process": "Silver Plating",
    "Operators": "Operator83, Operator146",
    "Tooling": "Tool27",
    "BatchSize": 149,
    "Quantity": 1359
  },
  {
    "WorkorderID": 122,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 06:30",
    "EndDateTime": "2024-10-02 14:30",
    "Process": "Polishing",
    "Operators": "Operator37, Operator80, Operator108, Operator113",
    "Tooling": "Tool15, Tool7, Tool5",
    "BatchSize": 149,
    "Quantity": 1359
  },
  {
    "WorkorderID": 122,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 05:36",
    "EndDateTime": "2024-10-03 09:36",
    "Process": "Conditioning",
    "Operators": "Operator142, Operator117, Operator35, Operator5",
    "Tooling": "Tool16, Tool15, Tool21",
    "BatchSize": 149,
    "Quantity": 1359
  },
  {
    "WorkorderID": 123,
    "Product": "Candlestick",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator142, Operator2, Operator38",
    "Tooling": "Tool15, Tool24, Tool2",
    "BatchSize": 114,
    "Quantity": 1474
  },
  {
    "WorkorderID": 123,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-01 23:06",
    "EndDateTime": "2024-10-02 03:06",
    "Process": "Preparing",
    "Operators": "Operator26, Operator6, Operator95",
    "Tooling": "Tool14, Tool2, Tool19",
    "BatchSize": 114,
    "Quantity": 1474
  },
  {
    "WorkorderID": 123,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-02 16:12",
    "EndDateTime": "2024-10-02 23:12",
    "Process": "Silver Plating",
    "Operators": "Operator136, Operator129",
    "Tooling": "Tool5, Tool4",
    "BatchSize": 114,
    "Quantity": 1474
  },
  {
    "WorkorderID": 123,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 09:12",
    "EndDateTime": "2024-10-03 12:12",
    "Process": "Polishing",
    "Operators": "Operator97, Operator143",
    "Tooling": "Tool6",
    "BatchSize": 114,
    "Quantity": 1474
  },
  {
    "WorkorderID": 123,
    "Product": "Candlestick",
    "StartDateTime": "2024-10-03 19:30",
    "EndDateTime": "2024-10-03 23:30",
    "Process": "Conditioning",
    "Operators": "Operator5",
    "Tooling": "Tool12, Tool25, Tool23",
    "BatchSize": 114,
    "Quantity": 1474
  },
  {
    "WorkorderID": 124,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator148, Operator75, Operator18",
    "Tooling": "Tool21",
    "BatchSize": 75,
    "Quantity": 1088
  },
  {
    "WorkorderID": 124,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 18:57",
    "EndDateTime": "2024-10-02 01:57",
    "Process": "Preparing",
    "Operators": "Operator1, Operator57",
    "Tooling": "Tool6, Tool7, Tool8",
    "BatchSize": 75,
    "Quantity": 1088
  },
  {
    "WorkorderID": 124,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 05:37",
    "EndDateTime": "2024-10-02 07:37",
    "Process": "Silver Plating",
    "Operators": "Operator75, Operator47",
    "Tooling": "Tool10, Tool26",
    "BatchSize": 75,
    "Quantity": 1088
  },
  {
    "WorkorderID": 124,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 03:22",
    "EndDateTime": "2024-10-03 09:22",
    "Process": "Polishing",
    "Operators": "Operator82",
    "Tooling": "Tool25, Tool3",
    "BatchSize": 75,
    "Quantity": 1088
  },
  {
    "WorkorderID": 124,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 11:10",
    "EndDateTime": "2024-10-03 14:10",
    "Process": "Conditioning",
    "Operators": "Operator88, Operator143, Operator36, Operator59",
    "Tooling": "Tool25, Tool2, Tool18",
    "BatchSize": 75,
    "Quantity": 1088
  },
  {
    "WorkorderID": 125,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator142",
    "Tooling": "Tool6, Tool7, Tool26",
    "BatchSize": 83,
    "Quantity": 1396
  },
  {
    "WorkorderID": 125,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 16:45",
    "EndDateTime": "2024-10-01 18:45",
    "Process": "Preparing",
    "Operators": "Operator11, Operator8, Operator9, Operator76",
    "Tooling": "Tool4",
    "BatchSize": 83,
    "Quantity": 1396
  },
  {
    "WorkorderID": 125,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 06:46",
    "EndDateTime": "2024-10-02 07:46",
    "Process": "Silver Plating",
    "Operators": "Operator119, Operator8, Operator29, Operator59, Operator88",
    "Tooling": "Tool10",
    "BatchSize": 83,
    "Quantity": 1396
  },
  {
    "WorkorderID": 125,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 07:59",
    "EndDateTime": "2024-10-02 11:59",
    "Process": "Polishing",
    "Operators": "Operator126, Operator110, Operator59, Operator130",
    "Tooling": "Tool27, Tool25, Tool10",
    "BatchSize": 83,
    "Quantity": 1396
  },
  {
    "WorkorderID": 125,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 13:25",
    "EndDateTime": "2024-10-02 19:25",
    "Process": "Conditioning",
    "Operators": "Operator45, Operator34, Operator150, Operator132, Operator99",
    "Tooling": "Tool26",
    "BatchSize": 83,
    "Quantity": 1396
  },
  {
    "WorkorderID": 126,
    "Product": "Cup",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator50, Operator40, Operator150",
    "Tooling": "Tool18",
    "BatchSize": 56,
    "Quantity": 624
  },
  {
    "WorkorderID": 126,
    "Product": "Cup",
    "StartDateTime": "2024-10-01 09:14",
    "EndDateTime": "2024-10-01 13:14",
    "Process": "Preparing",
    "Operators": "Operator62, Operator120, Operator116, Operator145",
    "Tooling": "Tool6",
    "BatchSize": 56,
    "Quantity": 624
  },
  {
    "WorkorderID": 126,
    "Product": "Cup",
    "StartDateTime": "2024-10-01 15:01",
    "EndDateTime": "2024-10-01 22:01",
    "Process": "Silver Plating",
    "Operators": "Operator140, Operator72, Operator24",
    "Tooling": "Tool10, Tool11",
    "BatchSize": 56,
    "Quantity": 624
  },
  {
    "WorkorderID": 126,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 09:10",
    "EndDateTime": "2024-10-02 11:10",
    "Process": "Polishing",
    "Operators": "Operator27, Operator36, Operator62",
    "Tooling": "Tool21, Tool18, Tool7",
    "BatchSize": 56,
    "Quantity": 624
  },
  {
    "WorkorderID": 126,
    "Product": "Cup",
    "StartDateTime": "2024-10-02 23:36",
    "EndDateTime": "2024-10-03 05:36",
    "Process": "Conditioning",
    "Operators": "Operator81, Operator119, Operator12, Operator34",
    "Tooling": "Tool21, Tool19",
    "BatchSize": 56,
    "Quantity": 624
  },
  {
    "WorkorderID": 127,
    "Product": "Goblet",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator15",
    "Tooling": "Tool9",
    "BatchSize": 106,
    "Quantity": 1168
  },
  {
    "WorkorderID": 127,
    "Product": "Goblet",
    "StartDateTime": "2024-10-01 11:52",
    "EndDateTime": "2024-10-01 17:52",
    "Process": "Preparing",
    "Operators": "Operator140",
    "Tooling": "Tool20, Tool23",
    "BatchSize": 106,
    "Quantity": 1168
  },
  {
    "WorkorderID": 127,
    "Product": "Goblet",
    "StartDateTime": "2024-10-02 17:14",
    "EndDateTime": "2024-10-03 01:14",
    "Process": "Silver Plating",
    "Operators": "Operator125, Operator73, Operator141, Operator65",
    "Tooling": "Tool30, Tool19, Tool15",
    "BatchSize": 106,
    "Quantity": 1168
  },
  {
    "WorkorderID": 127,
    "Product": "Goblet",
    "StartDateTime": "2024-10-03 06:33",
    "EndDateTime": "2024-10-03 07:33",
    "Process": "Polishing",
    "Operators": "Operator56",
    "Tooling": "Tool22",
    "BatchSize": 106,
    "Quantity": 1168
  },
  {
    "WorkorderID": 127,
    "Product": "Goblet",
    "StartDateTime": "2024-10-04 06:08",
    "EndDateTime": "2024-10-04 11:08",
    "Process": "Conditioning",
    "Operators": "Operator107, Operator124",
    "Tooling": "Tool22",
    "BatchSize": 106,
    "Quantity": 1168
  },
  {
    "WorkorderID": 128,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator9, Operator16, Operator133, Operator46, Operator146",
    "Tooling": "Tool4, Tool11, Tool7",
    "BatchSize": 75,
    "Quantity": 1330
  },
  {
    "WorkorderID": 128,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 07:32",
    "EndDateTime": "2024-10-01 09:32",
    "Process": "Preparing",
    "Operators": "Operator101",
    "Tooling": "Tool19, Tool10, Tool25",
    "BatchSize": 75,
    "Quantity": 1330
  },
  {
    "WorkorderID": 128,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 22:13",
    "EndDateTime": "2024-10-02 01:13",
    "Process": "Silver Plating",
    "Operators": "Operator17, Operator66, Operator96, Operator9",
    "Tooling": "Tool5",
    "BatchSize": 75,
    "Quantity": 1330
  },
  {
    "WorkorderID": 128,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 19:06",
    "EndDateTime": "2024-10-02 21:06",
    "Process": "Polishing",
    "Operators": "Operator119",
    "Tooling": "Tool3, Tool11, Tool1",
    "BatchSize": 75,
    "Quantity": 1330
  },
  {
    "WorkorderID": 128,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 03:45",
    "EndDateTime": "2024-10-03 11:45",
    "Process": "Conditioning",
    "Operators": "Operator25, Operator129, Operator95, Operator22",
    "Tooling": "Tool16",
    "BatchSize": 75,
    "Quantity": 1330
  },
  {
    "WorkorderID": 129,
    "Product": "Mug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator16, Operator99, Operator128",
    "Tooling": "Tool15, Tool27",
    "BatchSize": 65,
    "Quantity": 1164
  },
  {
    "WorkorderID": 129,
    "Product": "Mug",
    "StartDateTime": "2024-10-01 10:37",
    "EndDateTime": "2024-10-01 18:37",
    "Process": "Preparing",
    "Operators": "Operator2, Operator105, Operator43",
    "Tooling": "Tool15, Tool18",
    "BatchSize": 65,
    "Quantity": 1164
  },
  {
    "WorkorderID": 129,
    "Product": "Mug",
    "StartDateTime": "2024-10-02 17:42",
    "EndDateTime": "2024-10-03 00:42",
    "Process": "Silver Plating",
    "Operators": "Operator132, Operator102",
    "Tooling": "Tool14, Tool22, Tool12",
    "BatchSize": 65,
    "Quantity": 1164
  },
  {
    "WorkorderID": 129,
    "Product": "Mug",
    "StartDateTime": "2024-10-03 21:13",
    "EndDateTime": "2024-10-03 23:13",
    "Process": "Polishing",
    "Operators": "Operator61, Operator89, Operator51",
    "Tooling": "Tool30, Tool10, Tool2",
    "BatchSize": 65,
    "Quantity": 1164
  },
  {
    "WorkorderID": 129,
    "Product": "Mug",
    "StartDateTime": "2024-10-04 15:21",
    "EndDateTime": "2024-10-04 18:21",
    "Process": "Conditioning",
    "Operators": "Operator141",
    "Tooling": "Tool11",
    "BatchSize": 65,
    "Quantity": 1164
  },
  {
    "WorkorderID": 130,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator25, Operator87",
    "Tooling": "Tool16, Tool12, Tool27",
    "BatchSize": 119,
    "Quantity": 922
  },
  {
    "WorkorderID": 130,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 21:45",
    "EndDateTime": "2024-10-02 01:45",
    "Process": "Preparing",
    "Operators": "Operator80",
    "Tooling": "Tool13, Tool21, Tool8",
    "BatchSize": 119,
    "Quantity": 922
  },
  {
    "WorkorderID": 130,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 05:31",
    "EndDateTime": "2024-10-02 13:31",
    "Process": "Silver Plating",
    "Operators": "Operator127",
    "Tooling": "Tool13, Tool23",
    "BatchSize": 119,
    "Quantity": 922
  },
  {
    "WorkorderID": 130,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 14:53",
    "EndDateTime": "2024-10-02 22:53",
    "Process": "Polishing",
    "Operators": "Operator84, Operator6, Operator90",
    "Tooling": "Tool27, Tool8, Tool7",
    "BatchSize": 119,
    "Quantity": 922
  },
  {
    "WorkorderID": 130,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 05:30",
    "EndDateTime": "2024-10-03 13:30",
    "Process": "Conditioning",
    "Operators": "Operator44, Operator79, Operator80",
    "Tooling": "Tool13, Tool19, Tool24",
    "BatchSize": 119,
    "Quantity": 922
  },
  {
    "WorkorderID": 131,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator144, Operator97, Operator81, Operator80, Operator95",
    "Tooling": "Tool4, Tool22, Tool28",
    "BatchSize": 109,
    "Quantity": 867
  },
  {
    "WorkorderID": 131,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 08:43",
    "EndDateTime": "2024-10-01 13:43",
    "Process": "Preparing",
    "Operators": "Operator77, Operator45, Operator32, Operator120, Operator122",
    "Tooling": "Tool1, Tool14, Tool10",
    "BatchSize": 109,
    "Quantity": 867
  },
  {
    "WorkorderID": 131,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 10:55",
    "EndDateTime": "2024-10-02 12:55",
    "Process": "Silver Plating",
    "Operators": "Operator130, Operator51",
    "Tooling": "Tool19, Tool7",
    "BatchSize": 109,
    "Quantity": 867
  },
  {
    "WorkorderID": 131,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 23:20",
    "EndDateTime": "2024-10-03 01:20",
    "Process": "Polishing",
    "Operators": "Operator125, Operator68",
    "Tooling": "Tool23, Tool16",
    "BatchSize": 109,
    "Quantity": 867
  },
  {
    "WorkorderID": 131,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 20:55",
    "EndDateTime": "2024-10-03 21:55",
    "Process": "Conditioning",
    "Operators": "Operator24, Operator71, Operator26, Operator110",
    "Tooling": "Tool6, Tool30",
    "BatchSize": 109,
    "Quantity": 867
  },
  {
    "WorkorderID": 132,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator146",
    "Tooling": "Tool8",
    "BatchSize": 52,
    "Quantity": 1453
  },
  {
    "WorkorderID": 132,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 17:46",
    "EndDateTime": "2024-10-01 20:46",
    "Process": "Preparing",
    "Operators": "Operator89, Operator138, Operator117",
    "Tooling": "Tool28, Tool25",
    "BatchSize": 52,
    "Quantity": 1453
  },
  {
    "WorkorderID": 132,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 18:28",
    "EndDateTime": "2024-10-02 20:28",
    "Process": "Silver Plating",
    "Operators": "Operator110, Operator133, Operator21, Operator86",
    "Tooling": "Tool27, Tool7, Tool20",
    "BatchSize": 52,
    "Quantity": 1453
  },
  {
    "WorkorderID": 132,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 07:29",
    "EndDateTime": "2024-10-03 11:29",
    "Process": "Polishing",
    "Operators": "Operator86, Operator75, Operator64, Operator15, Operator109",
    "Tooling": "Tool12, Tool20, Tool16",
    "BatchSize": 52,
    "Quantity": 1453
  },
  {
    "WorkorderID": 132,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 22:25",
    "EndDateTime": "2024-10-04 04:25",
    "Process": "Conditioning",
    "Operators": "Operator63, Operator137",
    "Tooling": "Tool7",
    "BatchSize": 52,
    "Quantity": 1453
  },
  {
    "WorkorderID": 133,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator72",
    "Tooling": "Tool14, Tool26",
    "BatchSize": 83,
    "Quantity": 802
  },
  {
    "WorkorderID": 133,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 20:11",
    "EndDateTime": "2024-10-02 00:11",
    "Process": "Preparing",
    "Operators": "Operator91, Operator57, Operator116, Operator51",
    "Tooling": "Tool27, Tool24",
    "BatchSize": 83,
    "Quantity": 802
  },
  {
    "WorkorderID": 133,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 21:04",
    "EndDateTime": "2024-10-03 03:04",
    "Process": "Silver Plating",
    "Operators": "Operator81, Operator123, Operator57",
    "Tooling": "Tool28, Tool29, Tool19",
    "BatchSize": 83,
    "Quantity": 802
  },
  {
    "WorkorderID": 133,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 11:11",
    "EndDateTime": "2024-10-03 17:11",
    "Process": "Polishing",
    "Operators": "Operator111, Operator80, Operator16",
    "Tooling": "Tool16, Tool13",
    "BatchSize": 83,
    "Quantity": 802
  },
  {
    "WorkorderID": 133,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-04 10:20",
    "EndDateTime": "2024-10-04 13:20",
    "Process": "Conditioning",
    "Operators": "Operator15, Operator79, Operator147, Operator83, Operator78",
    "Tooling": "Tool20, Tool9, Tool13",
    "BatchSize": 83,
    "Quantity": 802
  },
  {
    "WorkorderID": 134,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator59",
    "Tooling": "Tool1",
    "BatchSize": 79,
    "Quantity": 826
  },
  {
    "WorkorderID": 134,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 12:49",
    "EndDateTime": "2024-10-01 16:49",
    "Process": "Preparing",
    "Operators": "Operator106, Operator48",
    "Tooling": "Tool17",
    "BatchSize": 79,
    "Quantity": 826
  },
  {
    "WorkorderID": 134,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 06:06",
    "EndDateTime": "2024-10-02 10:06",
    "Process": "Silver Plating",
    "Operators": "Operator74, Operator54, Operator79, Operator127",
    "Tooling": "Tool4, Tool24",
    "BatchSize": 79,
    "Quantity": 826
  },
  {
    "WorkorderID": 134,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 01:51",
    "EndDateTime": "2024-10-03 03:51",
    "Process": "Polishing",
    "Operators": "Operator125",
    "Tooling": "Tool9, Tool21, Tool29",
    "BatchSize": 79,
    "Quantity": 826
  },
  {
    "WorkorderID": 134,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 15:50",
    "EndDateTime": "2024-10-03 22:50",
    "Process": "Conditioning",
    "Operators": "Operator81",
    "Tooling": "Tool23, Tool24",
    "BatchSize": 79,
    "Quantity": 826
  },
  {
    "WorkorderID": 135,
    "Product": "Spoon",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator94, Operator124, Operator60",
    "Tooling": "Tool18, Tool16, Tool1",
    "BatchSize": 103,
    "Quantity": 1186
  },
  {
    "WorkorderID": 135,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 02:22",
    "EndDateTime": "2024-10-02 09:22",
    "Process": "Preparing",
    "Operators": "Operator124",
    "Tooling": "Tool25, Tool26, Tool7",
    "BatchSize": 103,
    "Quantity": 1186
  },
  {
    "WorkorderID": 135,
    "Product": "Spoon",
    "StartDateTime": "2024-10-02 20:29",
    "EndDateTime": "2024-10-02 22:29",
    "Process": "Silver Plating",
    "Operators": "Operator34, Operator130, Operator57, Operator143",
    "Tooling": "Tool27, Tool2, Tool26",
    "BatchSize": 103,
    "Quantity": 1186
  },
  {
    "WorkorderID": 135,
    "Product": "Spoon",
    "StartDateTime": "2024-10-03 12:54",
    "EndDateTime": "2024-10-03 20:54",
    "Process": "Polishing",
    "Operators": "Operator18, Operator102",
    "Tooling": "Tool15, Tool26",
    "BatchSize": 103,
    "Quantity": 1186
  },
  {
    "WorkorderID": 135,
    "Product": "Spoon",
    "StartDateTime": "2024-10-04 12:46",
    "EndDateTime": "2024-10-04 16:46",
    "Process": "Conditioning",
    "Operators": "Operator63, Operator61, Operator143, Operator129, Operator92",
    "Tooling": "Tool19",
    "BatchSize": 103,
    "Quantity": 1186
  },
  {
    "WorkorderID": 136,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator149, Operator33, Operator86, Operator94, Operator138",
    "Tooling": "Tool24, Tool18, Tool26",
    "BatchSize": 118,
    "Quantity": 605
  },
  {
    "WorkorderID": 136,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 09:02",
    "EndDateTime": "2024-10-01 17:02",
    "Process": "Preparing",
    "Operators": "Operator110",
    "Tooling": "Tool30, Tool7",
    "BatchSize": 118,
    "Quantity": 605
  },
  {
    "WorkorderID": 136,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 13:49",
    "EndDateTime": "2024-10-02 15:49",
    "Process": "Silver Plating",
    "Operators": "Operator61, Operator32, Operator150, Operator11, Operator79",
    "Tooling": "Tool30",
    "BatchSize": 118,
    "Quantity": 605
  },
  {
    "WorkorderID": 136,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 14:23",
    "EndDateTime": "2024-10-03 19:23",
    "Process": "Polishing",
    "Operators": "Operator130, Operator93, Operator108, Operator111, Operator19",
    "Tooling": "Tool23, Tool18, Tool6",
    "BatchSize": 118,
    "Quantity": 605
  },
  {
    "WorkorderID": 136,
    "Product": "Bottle",
    "StartDateTime": "2024-10-04 10:56",
    "EndDateTime": "2024-10-04 13:56",
    "Process": "Conditioning",
    "Operators": "Operator112, Operator1, Operator124",
    "Tooling": "Tool9, Tool23",
    "BatchSize": 118,
    "Quantity": 605
  },
  {
    "WorkorderID": 137,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator150, Operator1, Operator75, Operator130, Operator140",
    "Tooling": "Tool29, Tool27",
    "BatchSize": 95,
    "Quantity": 834
  },
  {
    "WorkorderID": 137,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 02:18",
    "EndDateTime": "2024-10-02 03:18",
    "Process": "Preparing",
    "Operators": "Operator50",
    "Tooling": "Tool19, Tool25, Tool5",
    "BatchSize": 95,
    "Quantity": 834
  },
  {
    "WorkorderID": 137,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 02:33",
    "EndDateTime": "2024-10-03 06:33",
    "Process": "Silver Plating",
    "Operators": "Operator138, Operator30, Operator36, Operator8, Operator11",
    "Tooling": "Tool19, Tool11, Tool16",
    "BatchSize": 95,
    "Quantity": 834
  },
  {
    "WorkorderID": 137,
    "Product": "Vase",
    "StartDateTime": "2024-10-03 09:27",
    "EndDateTime": "2024-10-03 17:27",
    "Process": "Polishing",
    "Operators": "Operator99",
    "Tooling": "Tool22, Tool12",
    "BatchSize": 95,
    "Quantity": 834
  },
  {
    "WorkorderID": 137,
    "Product": "Vase",
    "StartDateTime": "2024-10-04 12:18",
    "EndDateTime": "2024-10-04 15:18",
    "Process": "Conditioning",
    "Operators": "Operator75",
    "Tooling": "Tool1, Tool23",
    "BatchSize": 95,
    "Quantity": 834
  },
  {
    "WorkorderID": 138,
    "Product": "Tumbler",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator141, Operator132, Operator90",
    "Tooling": "Tool20, Tool29, Tool17",
    "BatchSize": 134,
    "Quantity": 1113
  },
  {
    "WorkorderID": 138,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-01 12:07",
    "EndDateTime": "2024-10-01 17:07",
    "Process": "Preparing",
    "Operators": "Operator23",
    "Tooling": "Tool28",
    "BatchSize": 134,
    "Quantity": 1113
  },
  {
    "WorkorderID": 138,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-02 08:30",
    "EndDateTime": "2024-10-02 16:30",
    "Process": "Silver Plating",
    "Operators": "Operator110",
    "Tooling": "Tool29",
    "BatchSize": 134,
    "Quantity": 1113
  },
  {
    "WorkorderID": 138,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-03 04:50",
    "EndDateTime": "2024-10-03 09:50",
    "Process": "Polishing",
    "Operators": "Operator29",
    "Tooling": "Tool22",
    "BatchSize": 134,
    "Quantity": 1113
  },
  {
    "WorkorderID": 138,
    "Product": "Tumbler",
    "StartDateTime": "2024-10-04 03:40",
    "EndDateTime": "2024-10-04 08:40",
    "Process": "Conditioning",
    "Operators": "Operator139",
    "Tooling": "Tool5",
    "BatchSize": 134,
    "Quantity": 1113
  },
  {
    "WorkorderID": 139,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 04:00",
    "Process": "Forging",
    "Operators": "Operator73, Operator133, Operator5",
    "Tooling": "Tool30, Tool18",
    "BatchSize": 147,
    "Quantity": 991
  },
  {
    "WorkorderID": 139,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 04:07",
    "EndDateTime": "2024-10-01 12:07",
    "Process": "Preparing",
    "Operators": "Operator15, Operator51, Operator53, Operator58, Operator31",
    "Tooling": "Tool27, Tool23",
    "BatchSize": 147,
    "Quantity": 991
  },
  {
    "WorkorderID": 139,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 00:52",
    "EndDateTime": "2024-10-02 01:52",
    "Process": "Silver Plating",
    "Operators": "Operator132, Operator118",
    "Tooling": "Tool21, Tool18, Tool19",
    "BatchSize": 147,
    "Quantity": 991
  },
  {
    "WorkorderID": 139,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 11:31",
    "EndDateTime": "2024-10-02 17:31",
    "Process": "Polishing",
    "Operators": "Operator138, Operator124, Operator39, Operator87",
    "Tooling": "Tool25, Tool17, Tool10",
    "BatchSize": 147,
    "Quantity": 991
  },
  {
    "WorkorderID": 139,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 02:47",
    "EndDateTime": "2024-10-03 04:47",
    "Process": "Conditioning",
    "Operators": "Operator112",
    "Tooling": "Tool25, Tool30, Tool20",
    "BatchSize": 147,
    "Quantity": 991
  },
  {
    "WorkorderID": 140,
    "Product": "Bowl",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator74, Operator122, Operator19, Operator38",
    "Tooling": "Tool10",
    "BatchSize": 77,
    "Quantity": 863
  },
  {
    "WorkorderID": 140,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 10:15",
    "EndDateTime": "2024-10-01 18:15",
    "Process": "Preparing",
    "Operators": "Operator143, Operator70, Operator128, Operator76, Operator141",
    "Tooling": "Tool14, Tool11",
    "BatchSize": 77,
    "Quantity": 863
  },
  {
    "WorkorderID": 140,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 22:13",
    "EndDateTime": "2024-10-02 05:13",
    "Process": "Silver Plating",
    "Operators": "Operator21, Operator36, Operator42, Operator110",
    "Tooling": "Tool27, Tool14",
    "BatchSize": 77,
    "Quantity": 863
  },
  {
    "WorkorderID": 140,
    "Product": "Bowl",
    "StartDateTime": "2024-10-02 18:54",
    "EndDateTime": "2024-10-03 01:54",
    "Process": "Polishing",
    "Operators": "Operator57, Operator54, Operator35, Operator20, Operator116",
    "Tooling": "Tool4, Tool18, Tool8",
    "BatchSize": 77,
    "Quantity": 863
  },
  {
    "WorkorderID": 140,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 01:56",
    "EndDateTime": "2024-10-03 06:56",
    "Process": "Conditioning",
    "Operators": "Operator62, Operator61, Operator88, Operator53",
    "Tooling": "Tool10",
    "BatchSize": 77,
    "Quantity": 863
  },
  {
    "WorkorderID": 141,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator104, Operator128, Operator114",
    "Tooling": "Tool12",
    "BatchSize": 112,
    "Quantity": 1337
  },
  {
    "WorkorderID": 141,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-01 12:57",
    "EndDateTime": "2024-10-01 20:57",
    "Process": "Preparing",
    "Operators": "Operator94, Operator64",
    "Tooling": "Tool22",
    "BatchSize": 112,
    "Quantity": 1337
  },
  {
    "WorkorderID": 141,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 19:32",
    "EndDateTime": "2024-10-02 20:32",
    "Process": "Silver Plating",
    "Operators": "Operator104, Operator79, Operator150",
    "Tooling": "Tool25, Tool9",
    "BatchSize": 112,
    "Quantity": 1337
  },
  {
    "WorkorderID": 141,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-02 22:56",
    "EndDateTime": "2024-10-03 06:56",
    "Process": "Polishing",
    "Operators": "Operator38, Operator75, Operator102, Operator80",
    "Tooling": "Tool14, Tool20, Tool16",
    "BatchSize": 112,
    "Quantity": 1337
  },
  {
    "WorkorderID": 141,
    "Product": "Napkin Ring",
    "StartDateTime": "2024-10-03 10:40",
    "EndDateTime": "2024-10-03 14:40",
    "Process": "Conditioning",
    "Operators": "Operator104, Operator114, Operator149",
    "Tooling": "Tool14, Tool16, Tool11",
    "BatchSize": 112,
    "Quantity": 1337
  },
  {
    "WorkorderID": 142,
    "Product": "Bowl",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-09-30 23:00",
    "Process": "Forging",
    "Operators": "Operator94, Operator118, Operator77, Operator14",
    "Tooling": "Tool26, Tool27, Tool11",
    "BatchSize": 56,
    "Quantity": 972
  },
  {
    "WorkorderID": 142,
    "Product": "Bowl",
    "StartDateTime": "2024-10-01 19:14",
    "EndDateTime": "2024-10-02 01:14",
    "Process": "Preparing",
    "Operators": "Operator128, Operator30, Operator7, Operator125, Operator122",
    "Tooling": "Tool4, Tool30",
    "BatchSize": 56,
    "Quantity": 972
  },
  {
    "WorkorderID": 142,
    "Product": "Bowl",
    "StartDateTime": "2024-10-02 22:22",
    "EndDateTime": "2024-10-03 04:22",
    "Process": "Silver Plating",
    "Operators": "Operator4, Operator133, Operator117, Operator95, Operator69",
    "Tooling": "Tool22, Tool25",
    "BatchSize": 56,
    "Quantity": 972
  },
  {
    "WorkorderID": 142,
    "Product": "Bowl",
    "StartDateTime": "2024-10-03 07:57",
    "EndDateTime": "2024-10-03 10:57",
    "Process": "Polishing",
    "Operators": "Operator90, Operator53, Operator89",
    "Tooling": "Tool5, Tool22",
    "BatchSize": 56,
    "Quantity": 972
  },
  {
    "WorkorderID": 142,
    "Product": "Bowl",
    "StartDateTime": "2024-10-04 00:04",
    "EndDateTime": "2024-10-04 06:04",
    "Process": "Conditioning",
    "Operators": "Operator125, Operator105, Operator61, Operator90, Operator9",
    "Tooling": "Tool23",
    "BatchSize": 56,
    "Quantity": 972
  },
  {
    "WorkorderID": 143,
    "Product": "Vase",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 02:00",
    "Process": "Forging",
    "Operators": "Operator53, Operator43",
    "Tooling": "Tool18, Tool12, Tool30",
    "BatchSize": 73,
    "Quantity": 785
  },
  {
    "WorkorderID": 143,
    "Product": "Vase",
    "StartDateTime": "2024-10-01 22:45",
    "EndDateTime": "2024-10-02 00:45",
    "Process": "Preparing",
    "Operators": "Operator150, Operator54, Operator70",
    "Tooling": "Tool22",
    "BatchSize": 73,
    "Quantity": 785
  },
  {
    "WorkorderID": 143,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 03:15",
    "EndDateTime": "2024-10-02 05:15",
    "Process": "Silver Plating",
    "Operators": "Operator140, Operator24",
    "Tooling": "Tool13",
    "BatchSize": 73,
    "Quantity": 785
  },
  {
    "WorkorderID": 143,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 08:47",
    "EndDateTime": "2024-10-02 09:47",
    "Process": "Polishing",
    "Operators": "Operator36, Operator25",
    "Tooling": "Tool13, Tool20",
    "BatchSize": 73,
    "Quantity": 785
  },
  {
    "WorkorderID": 143,
    "Product": "Vase",
    "StartDateTime": "2024-10-02 10:52",
    "EndDateTime": "2024-10-02 12:52",
    "Process": "Conditioning",
    "Operators": "Operator8, Operator101",
    "Tooling": "Tool30, Tool23",
    "BatchSize": 73,
    "Quantity": 785
  },
  {
    "WorkorderID": 144,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator78, Operator79, Operator16",
    "Tooling": "Tool4",
    "BatchSize": 71,
    "Quantity": 836
  },
  {
    "WorkorderID": 144,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 10:19",
    "EndDateTime": "2024-10-01 11:19",
    "Process": "Preparing",
    "Operators": "Operator64, Operator124",
    "Tooling": "Tool8",
    "BatchSize": 71,
    "Quantity": 836
  },
  {
    "WorkorderID": 144,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 11:04",
    "EndDateTime": "2024-10-02 19:04",
    "Process": "Silver Plating",
    "Operators": "Operator29, Operator121, Operator136",
    "Tooling": "Tool17",
    "BatchSize": 71,
    "Quantity": 836
  },
  {
    "WorkorderID": 144,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 04:50",
    "EndDateTime": "2024-10-03 07:50",
    "Process": "Polishing",
    "Operators": "Operator82",
    "Tooling": "Tool22, Tool26, Tool16",
    "BatchSize": 71,
    "Quantity": 836
  },
  {
    "WorkorderID": 144,
    "Product": "Bottle",
    "StartDateTime": "2024-10-03 18:19",
    "EndDateTime": "2024-10-04 01:19",
    "Process": "Conditioning",
    "Operators": "Operator128, Operator121, Operator97",
    "Tooling": "Tool22",
    "BatchSize": 71,
    "Quantity": 836
  },
  {
    "WorkorderID": 145,
    "Product": "Bottle",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 01:00",
    "Process": "Forging",
    "Operators": "Operator24, Operator128, Operator136",
    "Tooling": "Tool22, Tool13, Tool21",
    "BatchSize": 71,
    "Quantity": 1306
  },
  {
    "WorkorderID": 145,
    "Product": "Bottle",
    "StartDateTime": "2024-10-01 10:27",
    "EndDateTime": "2024-10-01 15:27",
    "Process": "Preparing",
    "Operators": "Operator30, Operator43, Operator71",
    "Tooling": "Tool16, Tool3",
    "BatchSize": 71,
    "Quantity": 1306
  },
  {
    "WorkorderID": 145,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 13:33",
    "EndDateTime": "2024-10-02 15:33",
    "Process": "Silver Plating",
    "Operators": "Operator150, Operator19, Operator11, Operator137",
    "Tooling": "Tool29, Tool16, Tool18",
    "BatchSize": 71,
    "Quantity": 1306
  },
  {
    "WorkorderID": 145,
    "Product": "Bottle",
    "StartDateTime": "2024-10-02 21:49",
    "EndDateTime": "2024-10-03 05:49",
    "Process": "Polishing",
    "Operators": "Operator83, Operator41",
    "Tooling": "Tool25, Tool9",
    "BatchSize": 71,
    "Quantity": 1306
  },
  {
    "WorkorderID": 145,
    "Product": "Bottle",
    "StartDateTime": "2024-10-04 03:28",
    "EndDateTime": "2024-10-04 09:28",
    "Process": "Conditioning",
    "Operators": "Operator91, Operator137",
    "Tooling": "Tool20",
    "BatchSize": 71,
    "Quantity": 1306
  },
  {
    "WorkorderID": 146,
    "Product": "Jug",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 06:00",
    "Process": "Forging",
    "Operators": "Operator103, Operator124, Operator48",
    "Tooling": "Tool27, Tool5",
    "BatchSize": 94,
    "Quantity": 1037
  },
  {
    "WorkorderID": 146,
    "Product": "Jug",
    "StartDateTime": "2024-10-01 21:53",
    "EndDateTime": "2024-10-02 01:53",
    "Process": "Preparing",
    "Operators": "Operator90",
    "Tooling": "Tool29",
    "BatchSize": 94,
    "Quantity": 1037
  },
  {
    "WorkorderID": 146,
    "Product": "Jug",
    "StartDateTime": "2024-10-02 23:15",
    "EndDateTime": "2024-10-03 06:15",
    "Process": "Silver Plating",
    "Operators": "Operator148",
    "Tooling": "Tool28, Tool6, Tool13",
    "BatchSize": 94,
    "Quantity": 1037
  },
  {
    "WorkorderID": 146,
    "Product": "Jug",
    "StartDateTime": "2024-10-03 21:09",
    "EndDateTime": "2024-10-04 01:09",
    "Process": "Polishing",
    "Operators": "Operator62",
    "Tooling": "Tool25, Tool28, Tool2",
    "BatchSize": 94,
    "Quantity": 1037
  },
  {
    "WorkorderID": 146,
    "Product": "Jug",
    "StartDateTime": "2024-10-04 03:42",
    "EndDateTime": "2024-10-04 09:42",
    "Process": "Conditioning",
    "Operators": "Operator131, Operator128, Operator110, Operator61",
    "Tooling": "Tool21, Tool7, Tool13",
    "BatchSize": 94,
    "Quantity": 1037
  },
  {
    "WorkorderID": 147,
    "Product": "Teapot",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 03:00",
    "Process": "Forging",
    "Operators": "Operator92",
    "Tooling": "Tool4, Tool5",
    "BatchSize": 100,
    "Quantity": 1109
  },
  {
    "WorkorderID": 147,
    "Product": "Teapot",
    "StartDateTime": "2024-10-01 22:11",
    "EndDateTime": "2024-10-02 01:11",
    "Process": "Preparing",
    "Operators": "Operator90, Operator71",
    "Tooling": "Tool12, Tool16",
    "BatchSize": 100,
    "Quantity": 1109
  },
  {
    "WorkorderID": 147,
    "Product": "Teapot",
    "StartDateTime": "2024-10-02 19:29",
    "EndDateTime": "2024-10-02 22:29",
    "Process": "Silver Plating",
    "Operators": "Operator29, Operator57",
    "Tooling": "Tool4, Tool25",
    "BatchSize": 100,
    "Quantity": 1109
  },
  {
    "WorkorderID": 147,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 01:16",
    "EndDateTime": "2024-10-03 09:16",
    "Process": "Polishing",
    "Operators": "Operator98, Operator69, Operator101",
    "Tooling": "Tool10, Tool6",
    "BatchSize": 100,
    "Quantity": 1109
  },
  {
    "WorkorderID": 147,
    "Product": "Teapot",
    "StartDateTime": "2024-10-03 13:22",
    "EndDateTime": "2024-10-03 16:22",
    "Process": "Conditioning",
    "Operators": "Operator142, Operator74, Operator25",
    "Tooling": "Tool9, Tool15",
    "BatchSize": 100,
    "Quantity": 1109
  },
  {
    "WorkorderID": 148,
    "Product": "Pitcher",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator18, Operator77, Operator149, Operator92, Operator72",
    "Tooling": "Tool12, Tool23",
    "BatchSize": 127,
    "Quantity": 858
  },
  {
    "WorkorderID": 148,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-01 15:02",
    "EndDateTime": "2024-10-01 20:02",
    "Process": "Preparing",
    "Operators": "Operator122",
    "Tooling": "Tool10, Tool28",
    "BatchSize": 127,
    "Quantity": 858
  },
  {
    "WorkorderID": 148,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-02 16:05",
    "EndDateTime": "2024-10-02 18:05",
    "Process": "Silver Plating",
    "Operators": "Operator64, Operator136",
    "Tooling": "Tool2, Tool15, Tool5",
    "BatchSize": 127,
    "Quantity": 858
  },
  {
    "WorkorderID": 148,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-03 10:27",
    "EndDateTime": "2024-10-03 18:27",
    "Process": "Polishing",
    "Operators": "Operator80, Operator121",
    "Tooling": "Tool21",
    "BatchSize": 127,
    "Quantity": 858
  },
  {
    "WorkorderID": 148,
    "Product": "Pitcher",
    "StartDateTime": "2024-10-04 11:57",
    "EndDateTime": "2024-10-04 17:57",
    "Process": "Conditioning",
    "Operators": "Operator23",
    "Tooling": "Tool14",
    "BatchSize": 127,
    "Quantity": 858
  },
  {
    "WorkorderID": 149,
    "Product": "Plate",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 00:00",
    "Process": "Forging",
    "Operators": "Operator100, Operator27, Operator137, Operator77, Operator128",
    "Tooling": "Tool14, Tool16",
    "BatchSize": 90,
    "Quantity": 974
  },
  {
    "WorkorderID": 149,
    "Product": "Plate",
    "StartDateTime": "2024-10-01 20:05",
    "EndDateTime": "2024-10-01 22:05",
    "Process": "Preparing",
    "Operators": "Operator50, Operator106, Operator96, Operator52, Operator123",
    "Tooling": "Tool2, Tool15",
    "BatchSize": 90,
    "Quantity": 974
  },
  {
    "WorkorderID": 149,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 08:01",
    "EndDateTime": "2024-10-02 11:01",
    "Process": "Silver Plating",
    "Operators": "Operator90",
    "Tooling": "Tool2",
    "BatchSize": 90,
    "Quantity": 974
  },
  {
    "WorkorderID": 149,
    "Product": "Plate",
    "StartDateTime": "2024-10-02 19:24",
    "EndDateTime": "2024-10-02 23:24",
    "Process": "Polishing",
    "Operators": "Operator29, Operator88, Operator40, Operator15, Operator26",
    "Tooling": "Tool5, Tool22, Tool16",
    "BatchSize": 90,
    "Quantity": 974
  },
  {
    "WorkorderID": 149,
    "Product": "Plate",
    "StartDateTime": "2024-10-03 13:46",
    "EndDateTime": "2024-10-03 14:46",
    "Process": "Conditioning",
    "Operators": "Operator15, Operator104",
    "Tooling": "Tool12",
    "BatchSize": 90,
    "Quantity": 974
  },
  {
    "WorkorderID": 150,
    "Product": "Tray",
    "StartDateTime": "2024-09-30 22:00",
    "EndDateTime": "2024-10-01 05:00",
    "Process": "Forging",
    "Operators": "Operator38, Operator79, Operator7, Operator124",
    "Tooling": "Tool16, Tool3",
    "BatchSize": 122,
    "Quantity": 1476
  },
  {
    "WorkorderID": 150,
    "Product": "Tray",
    "StartDateTime": "2024-10-01 17:33",
    "EndDateTime": "2024-10-02 00:33",
    "Process": "Preparing",
    "Operators": "Operator118, Operator9",
    "Tooling": "Tool5, Tool9, Tool20",
    "BatchSize": 122,
    "Quantity": 1476
  },
  {
    "WorkorderID": 150,
    "Product": "Tray",
    "StartDateTime": "2024-10-02 23:29",
    "EndDateTime": "2024-10-03 01:29",
    "Process": "Silver Plating",
    "Operators": "Operator73, Operator51, Operator52, Operator13, Operator103",
    "Tooling": "Tool14",
    "BatchSize": 122,
    "Quantity": 1476
  },
  {
    "WorkorderID": 150,
    "Product": "Tray",
    "StartDateTime": "2024-10-03 11:57",
    "EndDateTime": "2024-10-03 16:57",
    "Process": "Polishing",
    "Operators": "Operator101, Operator122, Operator92, Operator13",
    "Tooling": "Tool9",
    "BatchSize": 122,
    "Quantity": 1476
  },
  {
    "WorkorderID": 150,
    "Product": "Tray",
    "StartDateTime": "2024-10-04 03:48",
    "EndDateTime": "2024-10-04 07:48",
    "Process": "Conditioning",
    "Operators": "Operator61, Operator128, Operator43, Operator66, Operator18",
    "Tooling": "Tool3, Tool9, Tool13",
    "BatchSize": 122,
    "Quantity": 1476
  }
]
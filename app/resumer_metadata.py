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
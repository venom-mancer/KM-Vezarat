from django.urls import path
from KnowledgeManagement import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    path("", views.login_view, name="loginRoute"),
    path("home/", views.home, name="home"),
    path("successfullsave", views.successfullsave, name="successfullsave"),
    path("successfullsubmit", views.successfullsubmit, name="successfullsubmit"),
    path("EditExperience/<int:id>", views.EditExperience, name="EditExperience"),
    path("DeleteExperience/<int:id>",
         views.DeleteExperience, name="DeleteExperience"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("user_list/", views.user_list, name="user_list"),
    path("RegisterTitle", views.RegisterTitle, name="RegisterTitle"),
    path("RegisterCause", views.RegisterCause, name="RegisterCause"),
    path("get_members", views.get_members, name="get_members"),
    path('get_title', views.get_title, name='get_title'),
    path("get_knowledge_category", views.get_knowledge_category,
         name="get_knowledge_category"),
    path("RegisterWhichAction", views.RegisterWhichAction,
         name="RegisterWhichAction"),
    path("RegisterHow", views.RegisterHow, name="RegisterHow"),
    path("RegisterResource", views.RegisterResource, name="RegisterResource"),
    path("RegisterEvaluation", views.RegisterEvaluation, name="RegisterEvaluation"),
    path("RegisterConditions", views.RegisterConditions, name="RegisterConditions"),
    path("RegisterResults", views.RegisterResults, name="RegisterResults"),
    path("RegisterUsedCases", views.RegisterUsedCases, name="RegisterUsedCases"),
    path("RegisterRisks", views.RegisterRisks, name="RegisterRisks"),
    path("RegisterUsers", views.RegisterUsers, name="RegisterUsers"),
    path("RegisterProblemPreventation", views.RegisterProblemPreventation,
         name="RegisterProblemPreventation"),
    path("RegisterKnowledgeOpportunities",
         views.RegisterKnowledgeOpportunities, name="RegisterProblemPreventation"),

    # ثبت دانش urls
    path("take_survey/<int:id>", views.take_survey, name='take_survey'),

    path("thinking_room/", views.thinking_room, name='thinking_room'),
    path("send_documentation/", views.documentation_view,
         name='send_documentation'),
    path("polls_test/", views.polls_test, name='polls_test'),

    path("inform_meeting/", views.inform_meeting, name='inform_meeting'),
    path("take_exam_list/", views.take_exam_list, name='take_exam_list'),
    path("take_exam/<int:id>", views.take_exam, name='take_exam'),
    path("exam_score/<int:id>", views.exam_score, name='exam_score'),
    path("exam_review/<int:id>", views.exam_review, name='exam_review'),
    path("test_list/", views.test_list, name='test_list'),
    path("inform_exam/<int:id>", views.inform_exam, name='inform_exam'),
    path("add_question/<int:id>", views.add_question, name='add_question'),
    path("question_list/<int:id>", views.question_list, name='question_list'),
    path("delete_question/<int:id>", views.delete_question, name='delete_question'),
    path("delete_exam/<int:id>", views.delete_exam, name='delete_exam'),
    path("send_test/<int:id>", views.send_test, name='send_test'),
    path("pros_and_cons_test/", views.pros_and_cons_test,
         name='pros_and_cons_test'),
    path("RegintserExperience/<int:type>", views.RegintserExperience,
         name="RegintserExperience"),

    path("saveVoiceKnowledge/", views.save_voice_knowledge,
         name="saveVoiceKnowledge"),

    path("removeVoice", views.remove_voice,
         name="removeVoice"),

    path("PermanentSubmit/<int:id>",
         views.permanent_submit, name='PermanentSubmit'),
    path("ItSendToEvaluator/<int:id>",
         views.It_send_to_evaluator, name='ItSendToEvaluator'),
    path("ItSendToExperts/<int:id>",
         views.It_send_to_experts, name='ItSendToExperts'),
    path("ItSendBackToKnowledgeWorker/<int:id>",
         views.It_send_back_to_knowledgeWorker, name='ItSendBackToKnowledgeWorker'),
    path("matchingknowledge/<int:id>",
         views.matchingknowledge, name="matchingknowledge"),
    path("EditChartNode/<int:id>", views.EditChartNode, name="EditChartNode"),
    path("UpdateChartNode", views.UpdateChartNode, name="UpdateChartNode"),
    path("document_list/", views.document_list, name="document_list"),
    path("DeleteChartNode/<int:id>", views.DeleteChartNode, name="DeleteChartNode"),
    path("KnowledgeList/<int:id>", views.KnowledgeList, name="KnowledgeList"),
    path("comparativeـknowledge/", views.comparativeـknowledge_list,
         name="comparativeـknowledge"),
    path("comparative_knowledge_view/<int:id>",
         views.comparative_knowledge_view, name="comparative_knowledge_view"),

    path("skillـexperience_list/", views.skillـexperience_list,
         name="skillـexperience_list"),
    path("skill_experience_view/<int:id>",
         views.skill_experience_view, name="skill_experience_view"),

    path("jobـpromotion/", views.jobـpromotion, name="jobـpromotion"),
    path("job_promotion_view/<int:id>",
         views.job_promotion_view, name="job_promotion_view"),

    path("KnowledgeReport/", views.KnowledgeReport, name="KnowledgeReport"),
    path("KnowledgeView/<int:id>", views.KnowledgeView, name="KnowledgeView"),

    path("ReportKnowledgeTree", views.ReportKnowledgeTree,
         name="ReportKnowledgeTree"),
    #     path("KnowledgeDocuments/<int:id>", views.KnowledgeDocuments,
    #          name="KnowledgeDocuments"),
    path('like', views.like_view, name='like'),
    path('Request_view/<int:id>', views.Request_view, name='Request_view'),
    path('sendKarbargreqKnowl/<int:id>',
         views.send_view, name='sendKarbargreqKnowl'),
    path("removeFile", views.remove_file_view, name="removeFile"),
    path("DeleteDocumentation/<int:id>",
         views.document_delete, name="DeleteDocumentation"),
    path("editDocumentation/<int:id>",
         views.documentation_edit_view, name="editDocumentation"),
    path("removeDocFile", views.remove_docFile_view, name="removeDocFile"),
    path("Recycle_Knowledge/<int:id>",
         views.Recycle_Knowledge, name="Recycle_Knowledge"),
    # مدیرت دانش urls
    path("DocumentView/<int:id>", views.DocumentView, name="DocumentView"),
    path("rejected_knowledgeView/<int:id>",
         views.rejected_knowledgeView, name="rejected_knowledgeView"),
    path("document_list/", views.document_list, name="document_list"),
    path("my_knowledge_list/<int:id>",
         views.my_knowledge_list, name="my_knowledge_list"),
    path("used_knowledge/", views.used_knowledge, name="used_knowledge"),


    # profile model urls
    path("profile", views.Profile, name="Profile"),
    path("userProfile/<int:id>", views.user_profile, name="userProfile"),
    path("follow_unfollow/<int:id>", views.follow_unfollow, name="follow_unfollow"),
    path("message/<int:id>", views.message, name="message"),
    path("send_message/", views.send_message, name="send_message"),
    path("message_recieve_updater/", views.message_recieve_updater,
         name="message_recieve_updater"),

    path("followers/", views.followers, name="followers"),
    path("followings/", views.followings, name="followings"),
    path("edit_edu_records", views.edu_records_docs, name="edit_edu_records"),
    path("edit_pro_degree", views.pro_degree_docs, name="edit_pro_degree"),
    path("edit_passed_trials", views.passed_trials_docs, name="edit_passed_trials"),
    path("edit_inventions", views.inventions_docs, name="edit_inventions"),
    path("edit_books", views.books_docs, name="edit_books"),
    path("edit_articles", views.articles_docs, name="edit_articles"),
    path("edit_skills", views.skills_docs, name="edit_skills"),
    path("edit_job_record", views.job_record_docs, name="edit_job_record"),
    path("enterAsothers/", views.enter_as_others, name="enterAsothers"),

    # حراست urls
    path("security/", views.security, name="security"),
    path("rejected_security/<int:id>",
         views.rejected_security, name="rejected_security"),
    path("accepted_by_security/<int:id>",
         views.accepted_by_security, name="accepted_by_security"),

    # دبیر خانه urls
    path("survey_generator/", views.survey_generator, name="survey_generator"),
    path("edit_survey/<int:id>", views.edit_survey, name="edit_survey"),
    path("survey_list/", views.survey_list, name="survey_list"),
    path("delete_survey/<int:id>", views.delete_survey, name="delete_survey"),
    path("send_survey/<int:id>", views.send_survey, name="send_survey"),
    path("my_surveys/", views.my_surveys, name="my_surveys"),
    path("knowledge_review/<int:id>",
         views.knowledge_review, name="knowledge_review"),
    path("test_generator/", views.test_generator, name="test_generator"),
    path("edit_exam/<int:id>", views.edit_exam, name="edit_exam"),
    path("edit_question/<int:id>", views.edit_question, name="edit_question"),
    path("pros_and_cons/", views.pros_and_cons, name="pros_and_cons"),
    path("polls/", views.polls, name="polls"),
    path("IT/<int:id>", views.IT, name="IT"),
    path("ITworker/", views.ITworker, name="ITworker"),
    path("Key_indicators/", views.Key_indicators, name="Key_indicators"),
    path("indicator_assessment/", views.indicator_assessment,
         name="indicator_assessment"),
    path("describe_experts/", views.describe_experts, name="describe_experts"),
    path("get_expert_areas/", views.get_expert_areas, name="get_expert_areas"),
    path("user_activity_report/", views.user_activity_report,
         name="user_activity_report"),
    path("edit_experts/", views.edit_experts, name="edit_experts"),
    path("view_experts_list/", views.view_experts_list, name="view_experts_list"),
    path("ItSendsBackToEvaluator/<int:id>",
         views.It_send_back_to_evaluator, name='ItSendsBackToEvaluator'),
    path("ItSendsBackToKnowledgeWorker/<int:id>",
         views.It_send_back_to_knowledgeWorker_review, name='ItSendsBackToKnowledgeWorker'),
    path("find_chart_tree_level3/", views.find_chart_tree_level3, name="find_chart_tree_level3"),
    path("topic2_view/", views.topic2_view, name="topic2_view"),
    path("topic3_view/", views.topic3_view, name="topic3_view"),
    path("indicator_assessment_list/", views.indicator_assessment_list,
         name="indicator_assessment_list"),
    path("edit_indicator_assessment/<int:id>",
         views.edit_indicator_assessment, name="edit_indicator_assessment"),
    path("delete_indicator/<int:id>",
         views.delete_indicator, name="delete_indicator"),
    path("define_3topics/", views.define_3topics, name="define_3topics"),
    path("DeleteTopicNode/<int:id>/<int:type>",
         views.delete_topic_node, name="DeleteTopicNode"),
    path("EditTopicNode/<int:id>/<int:type>/<str:text>",
         views.edit_topic_node, name="EditTopicNode"),
    path("advanced_chart/<int:id>", views.advanced_chart, name="advanced_chart"),
    path("delete_advanced_chart/<int:id>",
         views.delete_advanced_chart, name="delete_advanced_chart"),
    path("removeDocs", views.removeDocs, name="removeDocs"),
    path("inform/", views.inform, name="inform"),
    path("edit_inform/<int:id>", views.edit_inform, name="edit_inform"),
    path("inform_list/", views.inform_list, name="inform_list"),
    path("delete_inform/<int:id>", views.delete_inform, name="delete_inform"),
    path("score_formula/", views.score_formula, name="score_formula"),
    path("thinking_room_paperwork/<int:id>",
         views.thinking_room_paperwork, name="thinking_room_paperwork"),
    path("thinking_room_list/", views.thinking_room_list,
         name="thinking_room_list"),
    path("delete_thinking_room_record/<int:id>",
         views.delete_thinking_room_record, name="delete_thinking_room_record"),
    path("edit_thinking_room/<int:id>",
         views.edit_thinking_room, name="edit_thinking_room"),
    path("Key_indicators_list/", views.Key_indicators_list,
         name="Key_indicators_list"),
    path("edit_Key_indicators/<int:id>",
         views.edit_Key_indicators, name="edit_Key_indicators"),
    path("delete_Key_indicators/<int:id>",
         views.delete_Key_indicators, name="delete_Key_indicators"),
    path("calculate_valuable_knowledge/", views.calculate_valuable_knowledge_list,
         name="calculate_valuable_knowledge"),
    path("calculate_valuable_knowledge/<int:id>",
         views.calculate_valuable_knowledge, name="calculate_valuable_knowledge"),
    path("give_user_reward/", views.give_user_reward, name="give_user_reward"),
    path("get_user_score/", views.get_user_score, name="get_user_score"),

    # گزارش urls
    path("sorting_knowledge/", views.sorting_knowledge, name="sorting_knowledge"),
    path("testet_users/", views.testet_users, name="testet_users"),
    path("conversation_hall/", views.conversation_hall, name="conversation_hall"),
    path("list_conversation_hall/", views.list_conversation_hall,
         name="list_conversation_hall"),
    path("polled_users/", views.polled_users, name="polled_users"),
    path("valuable_knowledges/", views.valuable_knowledges,
         name="valuable_knowledges"),
    path("expert_review_report/<int:id>",
         views.expert_review_report, name="expert_review_report"),
    path("kpi_expert_review_report/<int:id>",
         views.kpi_expert_review_report, name="kpi_expert_review_report"),
    path("kpi_knowledges/<int:id>", views.kpi_knowledges, name="kpi_knowledges"),
    path("knowledge_decition_tree/", views.knowledge_decition_tree,
         name="knowledge_decition_tree"),
    path("indicator_key_report/", views.indicator_key_report,
         name="indicator_key_report"),
    path("list_indicator_keys/", views.list_indicator_keys,
         name="list_indicator_keys"),
    path("ideasAndCriticism/", views.ideasAndCriticism, name="ideasAndCriticism"),
    path("list_of_tests/<int:id>", views.list_of_tests, name="list_of_tests"),
    path("list_of_polls/", views.list_of_polls, name="list_of_polls"),
    path("list_of_ideasAndCriticism/", views.list_of_ideasAndCriticism,
         name="list_of_ideasAndCriticism"),
    path("superior_knowledge_workers/", views.superior_knowledge_workers,
         name="superior_knowledge_workers"),
    path("systemMembers/", views.system_members, name="systemMembers"),
    path("special_knowledgeWorkers/", views.special_knowledgeWorkers,
         name="special_knowledgeWorkers"),
    path("systemExperts/", views.system_experts, name="systemExperts"),
    path("system_expert_roles/<int:id>",
         views.system_expert_roles, name="system_expert_roles"),
    path("process_experts/", views.process_experts, name="process_experts"),
    path("survey_result/<int:id>", views.survey_result, name="survey_result"),
    path("score_of_users/", views.score_of_users, name="score_of_users"),
    path("report_reward_users/", views.report_reward_users,
         name="report_reward_users"),
    path("report_knowledge/", views.report_knowledge, name="report_knowledge"),
    path("compare_knowledge_percent/", views.compare_knowledge_percent,
         name="compare_knowledge_percent"),
    path("document_list_report/", views.document_list_report,
         name="document_list_report"),

    # تالار گفتمان urls
    path("question_request/", views.question_request, name="question_request"),
    path("question_recive/", views.question_recive, name="question_recive"),
    path("question_sent/", views.question_sent, name="question_sent"),
    path('knowledgeRequest/', views.knowledgeRequest_view, name='knowledgeRequest'),
    path('knowledgeRecive/', views.knowledgeRecive_view, name='knowledgeRecive'),
    path('knowledgeSent/', views.knowledgeSent_view, name='knowledgeSent'),
    path('knowledgeSentForum/<int:id>',
         views.knowledge_sent_forum, name='knowledgeSentForum'),
    path('QuestionSentForum/<int:id>',
         views.QuestionSentForum, name='QuestionSentForum'),
    path('likeKnowledgeRequest', views.like_knowledge_request,
         name='likeKnowledgeRequest'),
    path('likeQuestionRequest', views.likeQuestionRequest,
         name='likeQuestionRequest'),
    path('likeAnswerKnowledgeRequest', views.like_answer_knowledge_request,
         name='like_answer_knowledge_request'),
    path('likes_of_question_answers', views.likes_of_question_answers,
         name='likes_of_question_answers'),
    path('used_Question_Request/', views.used_Question_Request,
         name='used_Question_Request'),
    path("used_Question_knowledge/", views.used_Question_knowledge,
         name="used_Question_knowledge"),

    # password urls
    path('password/', auth_views.PasswordChangeView.as_view(template_name="change_password.html"),
         name="change_password"),
    path('password/password_changed/', auth_views.PasswordChangeDoneView.as_view(template_name="success_pass_changed.html"),
         name="password_change_done"),

    # خبرگان urls
    path("rate_knowledge/<int:id>", views.rate_knowledge, name="ChartManagment"),
    path("unconfirmed_knowledge/", views.unconfirmed_knowledge,
         name="unconfirmed_knowledge"),
    path("ChartManagment", views.ChartManagment, name="ChartManagment"),
    path("knowledge_rate_result/<int:id>",
         views.knowledge_rate_result, name="knowledge_rate_result"),

    # HOME
    path("used_knowlege", views.used_knowlege, name="used_knowlege"),
    path("chatroom/<int:id>", views.chatroom, name="chatroom"),
    path("notifications_homepage/", views.notifications_homepage,
         name="notifications_homepage"),

    # notification
    path("get_notif_count_km/", views.get_notif_count_km,
         name="get_notif_count_km"),


]

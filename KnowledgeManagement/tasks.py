from celery import shared_task
from .models import TblKnowledge,TblExpertReview
from APAUtility.LibAPADateTime import get_persian_date_normalized

@shared_task(bind=True)
def turn_exp_2_knowledge_expert(self):
    """ turns the experiences to knowledge that are pending for experts reviews(turns them to knowledge after 3 days if all experts dont give reviews) """

    # getting all the exps waiting for expert reviews
    pending_exps = TblKnowledge.objects.filter(register_status=5)

    today_date = get_persian_date_normalized()

    for exp in pending_exps:

        # all reviews for this exp
        expert_reviews = TblExpertReview.objects.filter(knowledge=exp).filter(
        set_number=exp.set_number).filter(Status__gte=1)


        if expert_reviews.count()>=2:

            # gives us the latest scores of experts for this knowledge
            all_experts_scores_this_knowledge = expert_reviews.values_list(
            'score', flat=True)

            all_experts_total_score = sum(
            all_experts_scores_this_knowledge)/len(all_experts_scores_this_knowledge)

            # getting the date of the first expert review
            first_expert_review_date = expert_reviews[0].create_date

            differ_date = today_date - first_expert_review_date

            # if 3 days passed from the exp waitng for other experts it automatically passes it or reject it
            if differ_date >=3:
                if all_experts_total_score >= 50:
                    exp.register_status = 7
                    exp.save()
                else:
                    exp.register_status = 6
                    exp.save()

    return "The job is done!"
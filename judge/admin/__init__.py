from django.contrib import admin

from judge.admin.comments import CommentAdmin
from judge.admin.contest import ContestTagAdmin, ContestAdmin, ContestParticipationAdmin
from judge.admin.interface import NavigationBarAdmin, BlogPostAdmin, SolutionAdmin, LicenseAdmin
from judge.admin.organization import OrganizationAdmin, OrganizationRequestAdmin
from judge.admin.problem import ProblemAdmin
from judge.admin.profile import ProfileAdmin
from judge.admin.runtime import JudgeAdmin, LanguageAdmin
from judge.admin.submission import SubmissionAdmin
from judge.admin.taxon import ProblemGroupAdmin, ProblemTypeAdmin
from judge.admin.ticket import TicketAdmin
from judge.models import Language, Profile, Problem, ProblemGroup, ProblemType, Submission, Comment, \
    MiscConfig, Judge, NavigationBar, Contest, ContestParticipation, Organization, BlogPost, \
    Solution, License, OrganizationRequest, ContestTag, Ticket

admin.site.register(Language, LanguageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(ProblemGroup, ProblemGroupAdmin)
admin.site.register(ProblemType, ProblemTypeAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(MiscConfig)
admin.site.register(NavigationBar, NavigationBarAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Contest, ContestAdmin)
admin.site.register(ContestTag, ContestTagAdmin)
admin.site.register(ContestParticipation, ContestParticipationAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(OrganizationRequest, OrganizationRequestAdmin)
admin.site.register(Ticket, TicketAdmin)

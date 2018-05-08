@rules.predicate
def is_post_author_or_editor(user, post):
    return user == post.post_author | rules.is_group_member('editors')


@rules.predicate
def is_author_or_moderator(user, comment):
    return user == comment.comment_author | rules.is_group_member('moderator') | is_post_author_or_editor


rules.add_rule('can_publish_post', rules.is_group_member('editors'))
rules.add_rule('can_edit_post', is_post_author_or_editor)
rules.add_rule('can_delete_post', is_post_author_or_editor)
# Commenting rules
rules.add_rule('can_create_comment', is_author_or_moderator)
rules.add_rule('can_edit_comment', is_author_or_moderator)
rules.add_rule('can_delete_comment', is_author_or_moderator)

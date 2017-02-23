from app.util.AuthUtil import *
from app.util import MongoUtil, JsonUtil


@app.route('/user/groups', methods=['GET'])
@authorized_required
def get_user_groups(user):
    """
    @api {get} /user/groups Get all groups that user is in
    @apiName Get user reading groups
    @apiGroup User

    @apiUse AuthorizationTokenHeader

    @apiSuccess {String} id User id
    @apiSuccess {Object[]} lists Lists data
    @apiSuccess {String} lists.id List id
    @apiSuccess {Boolean} lists.archived Archived list or not
    @apiSuccess {String} lists.name List name
    @apiSuccessExample {json} Response (Example):
        {
            "groups": [
                {
                    "id": "adlfajdls",
                    "name": "Awesome Group"
                }
            ]
        }

    @apiUse UnauthorizedAccessError
    @apiUse UserNotInGroup
    """
    groups = MongoUtil.get_user_groups(user)

    if groups is None:
        return jsonify(msg='User is not in any group'), 204

    app.logger.info('User {} Get groups at {}'.format(user, request.full_path))
    return jsonify(groups=[JsonUtil.serialize(g, only=('id', 'name')) for g in groups])

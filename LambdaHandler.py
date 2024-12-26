# AWSync youtube video
# part 1: https://www.youtube.com/watch?v=ybbQW6cLKEQ
# part 2: https://www.youtube.com/watch?v=DgavixR_w5Y
# GitHub Link: https://github.com/iam-veeramalla/devops-project-ideas/tree/main/python/aws/Ninja

# Resume mistakes corrections: 
# 1. add month and year to projects
# 2. Resume name : Mahadev Metre_DevOps Engineer.pdf
# 3. project description : 
#    1. use action words
#    2. Quantify your Achievements
#    3. Customize to the role
# 4. Title at the top of the resume ex: MAHADEV METRE | AWS DevOps Engineer

# Code:

import boto3

def get_volume_id_from_arn(volume_arn):
    #split the ARN using the colon (':') separator
    arn_parts = volume_arn.split(':')
    #The volume ID is the last part of the ARN after the 'volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context): 

    volume_arn = event['resources'][0] 
    volume_id = get_volume_id_from_arn(volume_arn) 

    ec2_client = boto3.client('ec2')
    response = ec2_client.modify_volume( 
        VolumeId=volume_id, 
        VolumeType='gp3', 
    ) 
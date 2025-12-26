import boto3

def lambda_handler(event, context):
    elbv2 = boto3.client('elbv2')
    sns = boto3.client('sns')

    TARGET_GROUP_ARN = "arn:aws:elasticloadbalancing:us-west-1:975050024946:targetgroup/shivani-backend-tg/f1667804ba6adf86"
    SNS_TOPIC_ARN = "arn:aws:sns:us-west-1:975050024946:Hari-elb-health-alerts"

    response = elbv2.describe_target_health(
        TargetGroupArn=TARGET_GROUP_ARN
    )

    unhealthy_targets = []

    for target in response['TargetHealthDescriptions']:
        state = target['TargetHealth']['State']
        instance_id = target['Target']['Id']

        if state != 'healthy':
            unhealthy_targets.append(f"{instance_id} ({state})")

    if unhealthy_targets:
        message = (
            "Unhealthy instances detected behind Load Balancer:\n"
            + "\n".join(unhealthy_targets)
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="ALB Unhealthy Instance Alert",
            Message=message
        )

        print(message)
    else:
        print("All instances are healthy")

    return {
        "statusCode": 200,
        "body": "Health check completed"
    }

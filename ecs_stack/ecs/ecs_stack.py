from aws_cdk import (core, aws_ecs as ecs, aws_ecr as ecr, aws_ec2 as ec2, aws_iam as iam, aws_logs)


class EcsDevopsCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        ecr_repository = ecr.Repository(self,  
                                        "jamal-repository", 
                                         repository_name="jamal-repository")


        vpc = ec2.Vpc(self,  "jamal-vpc",  max_azs=3)

        cluster = ecs.Cluster(self,  
					  "jamal-cluster", 
					  cluster_name="jamal-cluster",
					  vpc=vpc)
        
        execution_role = iam.Role(self,  
                                  "jamal-execution-role", 
                                  assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"), 
                                  role_name="jamal-execution-role")

        execution_role.add_to_policy(iam.PolicyStatement( effect=iam.Effect.ALLOW, 
                                                            resources=["*"], 
                                                            actions=["ecr:GetAuthorizationToken",  
                                                                     "ecr:BatchCheckLayerAvailability",
                                                                     "ecr:GetDownloadUrlForLayer",  
                                                                     "ecr:BatchGetImage",  
                                                                     "logs:CreateLogStream",  
                                                                     "logs:PutLogEvents"  ]  ))
        task_definition = ecs.FargateTaskDefinition(self,  
                                                    "jamal-task-definition", 
                                                    execution_role=execution_role, 
                                                    family="jamal-task-definition")
        
        container = task_definition.add_container("jamal-sandbox", 
                                                  image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"))
        service = ecs.FargateService(self,  
                                     "jamal-service", 
                                     cluster=cluster, 
                                     task_definition=task_definition, 
                                     service_name="jamal-service")
        
        log_group = aws_logs.LogGroup(self,
                                      "jamal-service-logs-groups",
                                      log_group_name="jamal-service-logs")

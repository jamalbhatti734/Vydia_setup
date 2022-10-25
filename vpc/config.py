from aws_cdk.aws_ec2 import RouterType, CfnSecurityGroup

# basic VPC configs
VPC = 'custom-vpc'

INTERNET_GATEWAY = 'internet-gateway'

KEY_PAIR_NAME = 'us-east-1-key'

REGION = 'us-east-1'

# route tables
PUBLIC_ROUTE_TABLE = 'public-route-table'

ROUTE_TABLES_ID_TO_ROUTES_MAP = {
    PUBLIC_ROUTE_TABLE: [
        {
            'destination_cidr_block': '0.0.0.0/0',
            'gateway_id': INTERNET_GATEWAY,
            'router_type': RouterType.GATEWAY
        }
    ],
}


# subnets and instances
PUBLIC_SUBNET = 'public-subnet'
PRIVATE_SUBNET = 'private-subnet'
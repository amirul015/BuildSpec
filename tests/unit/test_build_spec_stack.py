import aws_cdk as core
import aws_cdk.assertions as assertions

from build_spec.build_spec_stack import BuildSpecStack

# example tests. To run these tests, uncomment this file along with the example
# resource in build_spec/build_spec_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BuildSpecStack(app, "build-spec")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

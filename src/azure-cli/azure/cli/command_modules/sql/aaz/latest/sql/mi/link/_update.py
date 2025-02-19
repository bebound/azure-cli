# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "sql mi link update",
)
class Update(AAZCommand):
    """Update a Managed Instance link replication mode.

    :example: Update a Managed Instance link replication mode.
        az sql mi link update -g testrg --mi testcl --name link1 --replication-mode Sync
    """

    _aaz_info = {
        "version": "2023-08-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.sql/managedinstances/{}/distributedavailabilitygroups/{}", "2023-08-01-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.link_name = AAZStrArg(
            options=["-n", "--name", "--link-name"],
            help="Managed Instance link name.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.managed_instance_name = AAZStrArg(
            options=["--mi", "--instance-name", "--managed-instance", "--managed-instance-name"],
            help="The name of the managed instance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.replication_mode = AAZStrArg(
            options=["--replication-mode"],
            arg_group="Properties",
            help="Replication mode of the link",
            enum={"Async": "Async", "Sync": "Sync"},
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.DistributedAvailabilityGroupsUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DistributedAvailabilityGroupsUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/distributedAvailabilityGroups/{distributedAvailabilityGroupName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "distributedAvailabilityGroupName", self.ctx.args.link_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "managedInstanceName", self.ctx.args.managed_instance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-08-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("replicationMode", AAZStrType, ".replication_mode")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.databases = AAZListType()
            properties.distributed_availability_group_id = AAZStrType(
                serialized_name="distributedAvailabilityGroupId",
                flags={"read_only": True},
            )
            properties.distributed_availability_group_name = AAZStrType(
                serialized_name="distributedAvailabilityGroupName",
                flags={"read_only": True},
            )
            properties.failover_mode = AAZStrType(
                serialized_name="failoverMode",
            )
            properties.instance_availability_group_name = AAZStrType(
                serialized_name="instanceAvailabilityGroupName",
            )
            properties.instance_link_role = AAZStrType(
                serialized_name="instanceLinkRole",
            )
            properties.partner_availability_group_name = AAZStrType(
                serialized_name="partnerAvailabilityGroupName",
            )
            properties.partner_endpoint = AAZStrType(
                serialized_name="partnerEndpoint",
            )
            properties.partner_link_role = AAZStrType(
                serialized_name="partnerLinkRole",
                flags={"read_only": True},
            )
            properties.replication_mode = AAZStrType(
                serialized_name="replicationMode",
            )
            properties.seeding_mode = AAZStrType(
                serialized_name="seedingMode",
            )

            databases = cls._schema_on_200.properties.databases
            databases.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.databases.Element
            _element.connected_state = AAZStrType(
                serialized_name="connectedState",
                flags={"read_only": True},
            )
            _element.database_name = AAZStrType(
                serialized_name="databaseName",
            )
            _element.instance_redo_replication_lag_seconds = AAZIntType(
                serialized_name="instanceRedoReplicationLagSeconds",
                flags={"read_only": True},
            )
            _element.instance_replica_id = AAZStrType(
                serialized_name="instanceReplicaId",
                flags={"read_only": True},
            )
            _element.instance_send_replication_lag_seconds = AAZIntType(
                serialized_name="instanceSendReplicationLagSeconds",
                flags={"read_only": True},
            )
            _element.last_backup_lsn = AAZStrType(
                serialized_name="lastBackupLsn",
                flags={"read_only": True},
            )
            _element.last_backup_time = AAZStrType(
                serialized_name="lastBackupTime",
                flags={"read_only": True},
            )
            _element.last_commit_lsn = AAZStrType(
                serialized_name="lastCommitLsn",
                flags={"read_only": True},
            )
            _element.last_commit_time = AAZStrType(
                serialized_name="lastCommitTime",
                flags={"read_only": True},
            )
            _element.last_hardened_lsn = AAZStrType(
                serialized_name="lastHardenedLsn",
                flags={"read_only": True},
            )
            _element.last_hardened_time = AAZStrType(
                serialized_name="lastHardenedTime",
                flags={"read_only": True},
            )
            _element.last_received_lsn = AAZStrType(
                serialized_name="lastReceivedLsn",
                flags={"read_only": True},
            )
            _element.last_received_time = AAZStrType(
                serialized_name="lastReceivedTime",
                flags={"read_only": True},
            )
            _element.last_sent_lsn = AAZStrType(
                serialized_name="lastSentLsn",
                flags={"read_only": True},
            )
            _element.last_sent_time = AAZStrType(
                serialized_name="lastSentTime",
                flags={"read_only": True},
            )
            _element.most_recent_link_error = AAZStrType(
                serialized_name="mostRecentLinkError",
                flags={"read_only": True},
            )
            _element.partner_auth_cert_validity = AAZObjectType(
                serialized_name="partnerAuthCertValidity",
                flags={"read_only": True},
            )
            _element.partner_replica_id = AAZStrType(
                serialized_name="partnerReplicaId",
                flags={"read_only": True},
            )
            _element.replica_state = AAZStrType(
                serialized_name="replicaState",
                flags={"read_only": True},
            )
            _element.seeding_progress = AAZStrType(
                serialized_name="seedingProgress",
                flags={"read_only": True},
            )
            _element.synchronization_health = AAZStrType(
                serialized_name="synchronizationHealth",
                flags={"read_only": True},
            )

            partner_auth_cert_validity = cls._schema_on_200.properties.databases.Element.partner_auth_cert_validity
            partner_auth_cert_validity.certificate_name = AAZStrType(
                serialized_name="certificateName",
                flags={"read_only": True},
            )
            partner_auth_cert_validity.expiry_date = AAZStrType(
                serialized_name="expiryDate",
                flags={"read_only": True},
            )

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""


__all__ = ["Update"]

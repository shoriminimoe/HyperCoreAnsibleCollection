# Ansible Collection for Scale Computing HyperCore

The Ansible Collection for Scale Computing HyperCore ([HyperCore](https://www.scalecomputing.com/sc-hypercore))
a variety of Ansible content to help automate the management of Scale Computing HyperCore products.


<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.12**.

The collection should work with any Ansible version **>=2.9.10**,
but this is not granted.
<!--end requires_ansible-->

## Python version compatibility

This collection requires Python 3.8 or greater.

## HyperCore cluster API version compatibility

This collection has been tested against HyperCore cluster API version v9.1.14.208456.

## Included content

### Inventory plugins

<!--start Inventory plugin name list-->
<!-- generated by ./docs/helpers/generate_readme_fragment.py -->
| Inventory plugin name | Description |
| --- | --- |
| [scale_computing.hypercore.hypercore](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/hypercore.html) | Inventory source for Scale Computing HyperCore.  |
<!--end Inventory plugin name list-->

### Modules

<!--start Module name list-->
<!-- generated by ./docs/helpers/generate_readme_fragment.py -->
| Module name | Description |
| --- | --- |
| [scale_computing.hypercore.api](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/api.html) | API interaction with Scale Computing HyperCore  |
| [scale_computing.hypercore.iso](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/iso.html) | Manage ISO images on HyperCore API  |
| [scale_computing.hypercore.vm_params](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_params.html) | Manage VM's parameters  |
| [scale_computing.hypercore.support_tunnel_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/support_tunnel_info.html) | Checks status of the remote support tunnel.  |
| [scale_computing.hypercore.support_tunnel](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/support_tunnel.html) | Opens or closes remote support tunnel.  |
| [scale_computing.hypercore.vm_disk](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_disk.html) | Manage VM's disks  |
| [scale_computing.hypercore.dns_config](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/dns_config.html) | Modify DNS configuration on HyperCore API  |
| [scale_computing.hypercore.user](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/user.html) | Creates, updates or deletes local hypercore user accounts.  |
| [scale_computing.hypercore.vm_import](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_import.html) | Handles import of the virtual machine  |
| [scale_computing.hypercore.dns_config_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/dns_config_info.html) | List DNS configuration on HyperCore API  |
| [scale_computing.hypercore.node_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/node_info.html) | Returns information about the nodes in a cluster.  |
| [scale_computing.hypercore.time_server_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/time_server_info.html) | List Time Server configuration on HyperCore API.  |
| [scale_computing.hypercore.iso_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/iso_info.html) | Retrieve ISO images  |
| [scale_computing.hypercore.email_alert](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/email_alert.html) | Create, update, delete or send test emails to Email Alert Recipients on HyperCore API.  |
| [scale_computing.hypercore.vm_node_affinity](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_node_affinity.html) | Update virtual machine's node affinity  |
| [scale_computing.hypercore.certificate](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/certificate.html) | Handles cluster SSL certificates.  |
| [scale_computing.hypercore.registration_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/registration_info.html) | Retrieve information about cluster registration.  |
| [scale_computing.hypercore.vm_clone](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_clone.html) | Handles cloning of the VM  |
| [scale_computing.hypercore.vm_nic](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_nic.html) | Handles actions over network interfaces  |
| [scale_computing.hypercore.cluster_name](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/cluster_name.html) | Update cluster name.  |
| [scale_computing.hypercore.oidc_config](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/oidc_config.html) | Handles openID connect configuration.  |
| [scale_computing.hypercore.snapshot_schedule](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/snapshot_schedule.html) | Manage snap schedule to configure the desired schedule of snapshot creation.  |
| [scale_computing.hypercore.vm_boot_devices](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_boot_devices.html) | Manage HyperCore VM's boot devices  |
| [scale_computing.hypercore.syslog_server_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/syslog_server_info.html) | List Syslog servers on HyperCore API  |
| [scale_computing.hypercore.registration](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/registration.html) | Handles cluster registration.  |
| [scale_computing.hypercore.user_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/user_info.html) | Returns information about the users.  |
| [scale_computing.hypercore.vm_replication_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_replication_info.html) | Returns info about replication of a specific VM  |
| [scale_computing.hypercore.oidc_config_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/oidc_config_info.html) | Returns information about openID connect configuration.  |
| [scale_computing.hypercore.email_alert_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/email_alert_info.html) | List Email Alert Recipients on HyperCore API  |
| [scale_computing.hypercore.time_zone](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/time_zone.html) | Modify Time Zone configuration on HyperCore API  |
| [scale_computing.hypercore.vm_replication](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_replication.html) | Handles VM replications  |
| [scale_computing.hypercore.syslog_server](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/syslog_server.html) | Create, update or delete Syslog servers from HyperCore API.  |
| [scale_computing.hypercore.remote_cluster_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/remote_cluster_info.html) | Retrieve a list of remote clusters.  |
| [scale_computing.hypercore.cluster_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/cluster_info.html) | Retrieve cluster info.  |
| [scale_computing.hypercore.vm_export](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_export.html) | Handles export of the virtual machine  |
| [scale_computing.hypercore.virtual_disk_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/virtual_disk_info.html) | List DNS configuration on HyperCore API  |
| [scale_computing.hypercore.task_wait](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/task_wait.html) | Wait for a HyperCore TaskTag to be finished.  |
| [scale_computing.hypercore.time_zone_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/time_zone_info.html) | List Time Zone configuration on HyperCore API  |
| [scale_computing.hypercore.smtp](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/smtp.html) | Modify SMTP configuration on HyperCore API.  |
| [scale_computing.hypercore.vm_nic_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_nic_info.html) | Returns info about NIC  |
| [scale_computing.hypercore.smtp_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/smtp_info.html) | List SMTP configuration on HyperCore API.  |
| [scale_computing.hypercore.vm_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm_info.html) | Retrieve information about the VMs.  |
| [scale_computing.hypercore.snapshot_schedule_info](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/snapshot_schedule_info.html) | Retrieve information about an automated VM snapshot schedule.  |
| [scale_computing.hypercore.vm](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/vm.html) | Create, update or delete a VM.  |
| [scale_computing.hypercore.time_server](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/time_server.html) | Modify Time Zone configuration on HyperCore API  |
| [scale_computing.hypercore.cluster_shutdown](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs/modules/cluster_shutdown.html) | Shutdown the cluster.  |
<!--end Module name list-->

### Roles

<!--start Role name list-->
<!-- generated by ./docs/helpers/generate_readme_fragment.py -->
| Role name | Description |
| --- | --- |
| [scale_computing.hypercore.cluster_config](https://scalecomputing.github.io/HyperCoreAnsibleCollection-docs) | Configure HyperCore cluster  |
<!--end Role name list-->


# Examples

The [examples](https://github.com/ScaleComputing/HyperCoreAnsibleCollection/tree/main/examples)
subdirectory contains usage examples for individual modules.
Look at [examples/README.md](https://github.com/ScaleComputing/HyperCoreAnsibleCollection/tree/main/examples/README.md) to see how to use each example.

# Development

See [DEVELOPMENT.md](https://github.com/ScaleComputing/HyperCoreAnsibleCollection/tree/main/DEVELOPMENT.md).

# Infra Notes

This folder will store Terraform/Docker/MAAS automation referenced in *The
Omniversal Aether*. Suggested subfolders:

- `terraform/` — Cloudflare R2, D1, Workers, Vectorize, Pages.
- `maas/` — provisioning scripts for Ubuntu Server + container hosts.
- `docker/` — compose files for CMS previews + local stacks.

Document every environment variable and secret so CI/CD can reproduce the stack.

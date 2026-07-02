title: Fixing a CoreCLR Load Error in IIS with Self-Contained Deployment
date: January 15th, 2025
slug: fixing-a-core-clr-load-error-in-iis-with-self-contained-deployment
category: .NET + IIS
status: active

Today I learned how to resolve a tricky issue I encountered while hosting an ASP.NET Core application in IIS. The error was:

```text
Application '/LM/W3SVC/2/ROOT' with physical root 'C:\inetpub\wwwroot\xxx_dev4' failed to load coreclr.
```

## Diagnosing the Issue

This error pointed to a failure in loading the .NET Core Common Language Runtime (CoreCLR). It’s a common problem when the server is missing the correct version of the .NET runtime required by the application. After some investigation, I found these potential causes:

- The .NET Core Hosting Bundle wasn’t installed on the server.
- The required .NET runtime version wasn’t present.
- The application pool in IIS was misconfigured.
- There were potential permission issues for the application folder.

## The Self-Contained Solution

To avoid dependency on the server’s runtime installation, I decided to try publishing the application as Self-Contained from Visual Studio 2022. This method bundles the .NET runtime and all dependencies with the application, ensuring it runs regardless of the server’s configuration.

## Steps to Publish as Self-Contained

Here’s how I published my app as Self-Contained in Visual Studio 2022:

1. Right-click on the project in Solution Explorer and choose Publish.
2. In the Pick a publish target dialog, I selected Folder.
3. Clicked Next and Finish to confirm the target.
4. Opened the Settings in the Publish tab.
    - Changed Deployment Mode to Self-Contained.
    - Selected the appropriate Target Runtime for my server (e.g., win-x64).
5. Saved the settings and clicked Publish.

The published output included all the necessary files, including the .NET runtime, making the app ready to deploy to IIS without relying on the server’s runtime installation.

## Results

After deploying the self-contained package to IIS, the application ran successfully! The CoreCLR error was resolved because the app now used the bundled runtime instead of depending on the server’s configuration.

## Key Takeaways

- Self-Contained Deployment is a lifesaver when hosting environments lack the required .NET runtime.
- It’s a great way to ensure version isolation, as the app always runs with the specific runtime version it was built with.
- The tradeoff is a larger deployment package and manual updates for runtime patches.

## Conclusion

Publishing as Self-Contained eliminated the CoreCLR dependency on the server and saved me a lot of time. If you’re deploying .NET Core apps to environments where you don’t control the runtime installation, Self-Contained is the way to go!

Hope you found this useful!
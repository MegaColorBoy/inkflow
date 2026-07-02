title: Why Hangfire recurring jobs should always have stable IDs?
date: January 5th, 2026
slug: why-hangfire-recurring-jobs-should-always-have-stable-ids
category: C# + Hangfire
status: active

Recently, I learned that **not giving explicit IDs to Hangfire recurring jobs can silently create duplicates**.

When you call `RecurringJob.AddOrUpdate(...)` without a pre-defined ID, Hangfire auto-generates one based on the method expression. That sounds fine—until you deploy across multiple nodes or refactor your code.

In such cases, Hangfire may generate a *new derived ID*, while the old recurring job continues running in the background. The result? **Duplicate jobs executing on schedule**, often goes unnoticed.

## Simple fix

Make sure that you always pass a clear, human-readable ID:

```csharp
RecurringJob.AddOrUpdate<ICustomBackgroundServiceManager>(
    "payments:reconcile-3h", // Human-readable ID
    s => s.ResendPaymentReportToVendorHourly(),
    Cron.Hourly(3)
);
```

Next, ensure that overlaps are impossible in a multi-node setup by adding this attribute to your job method:

```csharp
[DisableConcurrentExecution(timeoutInSeconds: 3600)]
public Task ResendPaymentReportToVendorHourly() { /* ... */ }
```

This uses a **distributed lock** backed by Hangfire storage—so even with multiple nodes, only one execution runs at a time. If you’re wondering whether this locks the job for the full hour: **it doesn’t**. The timeout exists for crash-safety, not throttling.

After doing this, recurring jobs become much easier to reason about, identify, pause, or delete in a multi-node environment.

Hope you found this tip useful!
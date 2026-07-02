title: Remove Control Flags
date: June 16th, 2024
slug: remove-control-flags
category: C# + Clean Code + Refactoring
status: active

There are times when we write flags to control the flow of the program. I mean, it's good to use control flags (sometimes) but it's not necessary to be used in most cases. Like the one shown below:

```csharp
public bool HandlePaymentRecords(List<PaymentRecord> paymentRecords)
{
    bool isSuccessful = true;

    foreach(var paymentRecord in paymentRecords)
    {
        if(!ProcessPaymentRecord(paymentRecord))
        {
            isSuccessful = false;
            break;
        }
    }

    return isSuccessful;
}

```

The name of method states it's purpose but it seems a tad bit complicated and might confuse some developers who get on-board with it. 

Instead, you can make of use of a refactoring technique called **Remove Control Flags** and modify the method to look like this:


```csharp
public bool HandlePaymentProcess(List<PaymentRecord> paymentRecords)
{
    foreach(var paymentRecord in paymentRecords)
    {
        if(!ProcessPaymentRecord(paymentRecord))
        {
            return false;
        }
    }

    return true;
}

```

The logic is the same but now the code is now simplified, less complex to read and much more maintainable.

Less code is good code.

Hope this helps you out!
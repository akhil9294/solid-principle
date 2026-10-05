# SOLID Principles in Python

SOLID is a set of five object-oriented design principles that help create clean, maintainable, and scalable software.

## 1. Single Responsibility Principle (SRP)

A class should have only one responsibility and one reason to change.

**Benefits:**
- Easy to understand
- Easy to maintain
- Better code organization

---

## 2. Open/Closed Principle (OCP)

Software entities should be open for extension but closed for modification.

This means you should add new functionality by extending existing code instead of changing already tested code.

**Benefits:**
- Reduces risk of breaking existing functionality
- Makes applications easier to extend

---

## 3. Liskov Substitution Principle (LSP)

A child class should be able to replace its parent class without affecting the correctness of the program.

### Guidelines:
1. All child classes should properly implement the behavior defined by the parent/base class.
2. Method implementations should remain consistent with the parent class.
3. Return types and expected behavior should not change unexpectedly.

**Benefits:**
- Improves reliability
- Makes inheritance easier to use

---

## 4. Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods they do not use.

Instead of creating one large interface, split it into smaller and more specific interfaces.

**Benefits:**
- Reduces unnecessary implementations
- Makes code easier to maintain
- Simplifies adding new functionality

---

## 5. Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions.

This helps reduce tight coupling between components.

**Benefits:**
- Better flexibility
- Easier testing and maintenance
- More reusable code

---

## Summary

- **SRP** → One class, one responsibility.
- **OCP** → Extend functionality without modifying existing code.
- **LSP** → Child classes should work as replacements for parent classes.
- **ISP** → Create small and focused interfaces.
- **DIP** → Depend on abstractions, not concrete implementations.
